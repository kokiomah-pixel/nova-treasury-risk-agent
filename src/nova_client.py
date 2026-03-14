import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("NOVA_API_URL", "https://api.novaos.ai")
API_KEY = os.getenv("NOVA_API_KEY", "")

def get_mock_context():
    return {
        "epoch": 2461,
        "regime": "Elevated Fragility",
        "guardrail": {
            "severity": "medium",
            "advisory": "Reduce size and avoid low-liquidity venues"
        },
        "memory_context": {
            "sequence_type": "liquidity_deterioration_cycle",
            "consequence_pattern": "historically escalates to Stress within 3–6 epochs"
        }
    }

def get_context(asset: str, intent: str, size: int):
    headers = {}

    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    try:
        response = requests.get(
            f"{API_URL}/v1/context",
            params={
                "asset": asset,
                "intent": intent,
                "size": size
            },
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        return get_mock_context()
