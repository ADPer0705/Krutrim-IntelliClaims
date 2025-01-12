from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSubmitClaim(Action):
    def name(self) -> Text:
        return "action_submit_claim"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        category = tracker.get_slot("category")
        claim_id = tracker.get_slot("claim_id")

        if category and claim_id:
            dispatcher.utter_message(
                text=f"Your claim has been submitted successfully! Category: {category}, Claim ID: {claim_id}."
            )
        else:
            dispatcher.utter_message(
                text="It seems like some information is missing. Please try again."
            )

        return []
