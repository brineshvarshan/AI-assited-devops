from kubernetes import client, config


def load_k8s_config():
    """
    Load Kubernetes config.
    Works both locally (minikube) and inside cluster.
    """
    try:
        config.load_kube_config()
        print("🔧 Loaded local kubeconfig")
    except:
        config.load_incluster_config()
        print("🔧 Loaded in-cluster config")


def restart_pod(namespace="default"):
    """
    Restart ONE pod safely by deleting it.
    Kubernetes will recreate it automatically.
    """
    load_k8s_config()

    v1 = client.CoreV1Api()

    pods = v1.list_namespaced_pod(namespace)

    for pod in pods.items:
        pod_name = pod.metadata.name

        # ⚠️ SAFETY: Do not touch system pods
        if pod_name.startswith(("kube-", "prometheus", "coredns")):
            continue

        print(f"🔁 Restarting pod: {pod_name}")
        v1.delete_namespaced_pod(
            name=pod_name,
            namespace=namespace
        )
        break  # restart only ONE pod (safe)
