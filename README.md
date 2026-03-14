

# Nova Treasury Risk Agent

A minimal treasury risk agent example that queries **Sharpe Nova OS** before changing treasury posture.

This project demonstrates how treasury systems can use Nova decision context to:

- detect elevated fragility
- reduce deployment aggressiveness
- pause new risk under stress
- preserve governance discipline

Nova does not move treasury capital.  
Nova provides decision context before treasury actions.

---

# What This Repo Shows

This starter shows a simple treasury decision loop:

1. Evaluate a proposed treasury action
2. Query Nova decision context
3. Evaluate regime and guardrail
4. Decide whether to:
   - proceed
   - reduce exposure
   - pause deployment

This is a decision-support example only.

---

# Core Primitive

```python
ctx = nova.context()



Example logic:

```python
ctx = get_context(asset="cbBTC", intent="deploy_liquidity", size=50000)
action = decide_treasury_posture(ctx)

print("Regime:", ctx.get("regime"))
print("Guardrail:", ctx.get("guardrail", {}).get("advisory"))
print("Treasury posture:", action)
```

---

# Treasury Decision Model

The starter agent uses Nova in this way:

- Stress → pause
- Elevated Fragility → reduce deployment pace
- high severity guardrail → reduce exposure
- otherwise → proceed

Nova does not deploy capital.  
Execution remains external to Nova.

---

# Repository Structure

```
nova-treasury-risk-agent/
│
├ examples/
│   └── run_treasury_agent.py
│
├ src/
│   ├── nova_client.py
│   └── treasury_policy.py
│
├ .env.example
├ requirements.txt
├ README.md
└ LICENSE
```

---

# Quick Start

Install dependencies:

```
pip install -r requirements.txt
```

Run the example:

```
python examples/run_treasury_agent.py
```

---

# Environment

Create a `.env` file from `.env.example` and configure:

```
NOVA_API_URL=
NOVA_API_KEY=
```

---

# Nova API Role

This example uses Nova as decision-support infrastructure.

Nova may:

- classify market regime
- provide advisory guardrails
- expose historical memory context
- provide verification metadata

Nova must not:

- execute treasury reallocations
- rebalance capital automatically
- block treasury actions directly
- override downstream governance logic

---

# License

MIT
