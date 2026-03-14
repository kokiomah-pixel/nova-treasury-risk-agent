def decide_treasury_posture(ctx: dict) -> str:
    regime = ctx.get("regime")
    severity = ctx.get("guardrail", {}).get("severity")

    if regime == "Stress":
        return "pause"

    if regime == "Elevated Fragility":
        return "reduce_deployment"

    if severity == "high":
        return "reduce_exposure"

    return "proceed"
