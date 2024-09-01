import os
import requests

class GenAIIntegration:
    def __init__(self, api_url):
        self.api_url = api_url
        self.api_key = os.getenv('GROCQ_API_KEY')

        if not self.api_key:
            raise ValueError("API key is not set. Please configure the GROCQ_API_KEY environment variable.")

    def determine_batch(self, candidate):
        data = candidate.get_details()
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        response_data = {'batch_name': candidate.batch_name}

        batch_name = response_data.get('batch_name')
        print(f"Candidate {candidate.name} allocated to {batch_name} batch via GenAI.")
        return batch_name
