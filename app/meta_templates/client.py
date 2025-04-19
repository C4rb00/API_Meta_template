# app/services/meta_templates/client.py
import httpx

class MetaTemplateClient:
    def __init__(self, token, base_url_template):
        self.token = token
        self.base_url_template = base_url_template

    def send_template(self, phone_number_id, payload):
        url = self.base_url_template.format(phone_number_id=phone_number_id)
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        try:
            response = httpx.post(url, json=payload, headers=headers, timeout=10)
            return {
                "status": response.status_code,
                "response": response.json()
            }
        except Exception as e:
            return {
                "status": "error",
                "response": str(e)
            }
