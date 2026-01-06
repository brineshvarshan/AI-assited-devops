from datetime import datetime
from k8s_actions import restart_pod


def handle_action(decision):
    """
    Decide what action to take based on decision.
    SAFE but REAL Kubernetes actions.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status = decision.get("status")
    severity = decision.get("severity")
    issues = decision.get("issues", [])

    if status == "NORMAL":
        print(f"🟢 [{timestamp}] System healthy. No action needed.")

    elif status == "ISSUE":
        print(f"🟡 [{timestamp}] Issue detected!")
        print("   Severity:", severity)
        print("   Issues:", ", ".join(issues))

        if severity == "low":
            print("   👉 Action: Logged for observation")

        elif severity == "medium":
            print("   👉 Action: Restarting one pod (self-healing)")
            restart_pod()

        elif severity == "high":
            print("   🚨 Action: High severity detected (manual intervention required)")

    print("-" * 50)
