from src.nova_client import get_context
from src.treasury_policy import decide_treasury_posture

def main():
    ctx = get_context(asset="cbBTC", intent="deploy_liquidity", size=50000)
    action = decide_treasury_posture(ctx)

    print("Regime:", ctx.get("regime"))
    print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
    print("Treasury posture:", action)

if __name__ == "__main__":
    main()
