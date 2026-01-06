from metrics_collector import get_cluster_metrics
from decision_engine import analyze_metrics

metrics = get_cluster_metrics()
decision = analyze_metrics(metrics)

print("METRICS:", metrics)
print("DECISION:", decision)
