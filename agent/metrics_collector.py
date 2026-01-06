import requests

PROMETHEUS_URL = "http://prometheus-kube-prometheus-prometheus.default.svc.cluster.local:9090"


def query_prometheus(query):
    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query",
        params={"query": query}
    )
    return response.json()


def get_cluster_metrics():
    metrics = {}

    cpu_query = 'sum(rate(container_cpu_usage_seconds_total[5m]))'
    memory_query = 'sum(container_memory_working_set_bytes)'
    restart_query = 'sum(kube_pod_container_status_restarts_total)'

    cpu_data = query_prometheus(cpu_query)
    memory_data = query_prometheus(memory_query)
    restart_data = query_prometheus(restart_query)

    metrics["cpu_usage"] = float(cpu_data["data"]["result"][0]["value"][1])
    metrics["memory_usage_bytes"] = float(memory_data["data"]["result"][0]["value"][1])
    metrics["pod_restarts"] = int(float(restart_data["data"]["result"][0]["value"][1]))

    return metrics


if __name__ == "__main__":
    print(get_cluster_metrics())
