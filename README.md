

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
