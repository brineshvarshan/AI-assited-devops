import time

from metrics_collector import get_cluster_metrics
from decision_engine import analyze_metrics
from action_handler import handle_action

# How often the agent should check (in seconds)
CHECK_INTERVAL = 5


def run_agent():
    print("🤖 AI DevOps Agent started...")
    print("⏱ Monitoring interval:", CHECK_INTERVAL, "seconds")
    print("-" * 50)

    while True:
        try:
            # 1️⃣ OBSERVE: Collect metrics from Prometheus
            metrics = get_cluster_metrics()

            # 2️⃣ THINK: Analyze metrics and make decision
            decision = analyze_metrics(metrics)

            # 3️⃣ REPORT
            print("📊 METRICS:", metrics)
            print("🧠 DECISION:", decision)

            # 4️⃣ ACT (safe actions only)
            handle_action(decision)

        except Exception as e:
            print("❌ Agent error:", e)

        # 5️⃣ WAIT before next cycle
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    run_agent()
