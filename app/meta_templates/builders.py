import pandas as pd

class MetaTemplateComponentBuilder:
    @staticmethod
    def build_components(row):
        components = []

        if "header_text" in row and pd.notna(row["header_text"]):
            components.append({
                "type": "HEADER",
                "format": "TEXT",
                "text": row["header_text"]
            })

        components.append({
            "type": "BODY",
            "text": row["body"]
        })

        if "footer_text" in row and pd.notna(row["footer_text"]):
            components.append({
                "type": "FOOTER",
                "text": row["footer_text"]
            })

        return components

class MetaTemplatePayloadBuilder:
    @staticmethod
    def build_payload(row, components):
        return {
            "name": row["template_name"],
            "language": row["language"],
            "category": row["category"],
            "components": components
        }