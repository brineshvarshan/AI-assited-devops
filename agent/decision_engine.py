def analyze_metrics(metrics):
    """
    This function takes metrics and decides
    whether the cluster is healthy or not.
    """

    cpu = metrics.get("cpu_usage", 0)
    memory_bytes = metrics.get("memory_usage_bytes", 0)
    restarts = metrics.get("pod_restarts", 0)

    # Convert memory from bytes to GB (easy to understand)
    memory_gb = memory_bytes / 1024 / 1024 / 1024

    # Decision result
    decision = {
        "status": "NORMAL",
        "issues": [],
        "severity": "low"
    }

    # Rule 1: High CPU usage
    if cpu > 0.8:
        decision["status"] = "ISSUE"
        decision["issues"].append("High CPU usage")
        decision["severity"] = "medium"

    # Rule 2: High memory usage
    if memory_gb > 4:
        decision["status"] = "ISSUE"
        decision["issues"].append("High memory usage")
        decision["severity"] = "medium"

    # Rule 3: Too many restarts
    if restarts > 50:
        decision["status"] = "ISSUE"
        decision["issues"].append("Too many pod restarts")
        decision["severity"] = "low"

    return decision
