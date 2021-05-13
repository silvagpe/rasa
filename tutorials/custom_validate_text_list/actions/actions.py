import pathlib
from typing import Text, List, Any, Dict, Optional

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# Lista de nomes válidos
names = pathlib.Path("data/names.txt").read_text().split("\n")


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    # Permite adicionar slots como requeridos de forma programática
    #-----------------------------------------------------------------
    async def required_slots(
        self,

        #A lista de slots do domain
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:

        #Recupera o nome
        first_name = tracker.slots.get("first_name")
        print(f"required_slots: {first_name}");


        if tracker.get_slot("name_spelled_correctly"):
            return slots_mapped_in_domain   

        #Se existir valor 
        if first_name is not None:
            print(f"- check name...");
            #Valida se o nome não está na lista 
            if first_name not in names:
                print(f"- not found");
                return ["name_spelled_correctly"] + slots_mapped_in_domain

            print(f"- found");
            
        return slots_mapped_in_domain

    # Permite extrair valores de forma programatica
    # segue a mesma regra das outras Trigger
    # extract_<slot_name> ou extract_<form_name>_<slot_name>
    #-----------------------------------------------------------------
    async def extract_name_spelled_correctly(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:

        
        # Recupera a última intenção inputada
        intent = tracker.get_intent_of_latest_message()
        print(f"extract_name_spelled_correctly: {intent}");
        # Se a intenção for igual a "affirm" então marca o campo como correto
        return {"name_spelled_correctly": intent == "affirm"}

    # Permite validar o slot name_spelled_correctly
    # segue a mesma regra das outras Trigger
    # validate_<slot_name> ou validate_<form_name>_<slot_name>
    #-----------------------------------------------------------------
    def validate_name_spelled_correctly(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        first_name = tracker.get_slot("first_name")
        is_correct = tracker.get_slot("name_spelled_correctly");
        print(f"validate_name_spelled_correctly: {first_name} - {is_correct}");

        
        #Se estiver correto preenche o valor para o slot first_name
        if tracker.get_slot("name_spelled_correctly"):
            return {"first_name": tracker.get_slot("first_name"), "name_spelled_correctly": True}

        #Caso controário limpa o valor do slot
        return {"first_name": None, "name_spelled_correctly": None}


    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 1:
            dispatcher.utter_message(
                text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}


    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 1:
            dispatcher.utter_message(
                text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"last_name": None}
        else:
            return {"last_name": slot_value}
