# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionPizzaOrderForm(Action):

    def name(self) -> Text:
        return "action_pizza_order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["pizza_amount", "pizza_size", "pizza_type"]


    # def submit(
    #     self,
    #     tracker: Tracker,
    #     dispatcher: CollectingDispatcher,
    #     domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    #     pizza_type = tracker.get_slot('pizza_type');
    #     pizza_size = tracker.get_slot('pizza_size');
    #     pizza_amount = tracker.get_slot('pizza_amount');

    #     print(pizza_type, pizza_size, pizza_amount)

    #     dispatcher.utter_message(text=f"Ok great!. Your order is {pizza_amount} {pizza_type} pizza in {pizza_size} size. Can you please confirm your order?")

    #     return []


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pizza_type = tracker.get_slot('pizza_type');
        pizza_size = tracker.get_slot('pizza_size');
        pizza_amount = tracker.get_slot('pizza_amount');        
                    

        print(pizza_type, pizza_size, pizza_amount)

        dispatcher.utter_message(text=f"Ok great! Your order is {pizza_amount} {pizza_type} pizza in {pizza_size} size. Can you please confirm your order?")

        return []

    
