from app.services.meta_templates.client import MetaTemplateClient

class MetaTemplateProcessor:
    def __init__(self, client: MetaTemplateClient):
        self.client = client

    def process_templates(self, df):
        results = []

        for _, row in df.iterrows():
            payload = {
                "name": row["template_name"],
                "language": row["language"],
                "category": row["category"],
                "components": [
                    {"type": "BODY", "text": row["body"]}
                ]
            }

            phone_number_id = row.get("phone_number_id", "YOUR_PHONE_NUMBER_ID")
            result = self.client.send_template(phone_number_id, payload)
            result["template"] = row["template_name"]
            results.append(result)

        return results
