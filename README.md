# 🤖 AI-Assisted Kubernetes Monitoring & Decision Agent

<p align="center">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

<p align="center">
  <strong>A production-grade, safety-first DevOps monitoring agent that runs inside Kubernetes clusters, continuously analyzes infrastructure health using Prometheus metrics, and provides intelligent operational insights.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen" alt="Status"/>
  <img src="https://img.shields.io/badge/Safety-First-blue" alt="Safety"/>
  <img src="https://img.shields.io/badge/Observable-100%25-orange" alt="Observable"/>
</p>

---

## 🎯 **The Problem**

In modern Kubernetes environments, DevOps teams face critical challenges:

- ❌ **Manual monitoring doesn't scale** - Engineers can't watch 50+ pods 24/7
- ❌ **Reactive incident response** - Problems detected after failures occur
- ❌ **Alert fatigue** - Too many false positives hide real issues
- ❌ **Dangerous automation** - Blind auto-healing can cause cascading failures
- ❌ **Lack of context** - Raw metrics without intelligent analysis

**Industry Reality:** Most production outages aren't caused by lack of automation—they're caused by **unsafe automation**.

---

## 💡 **The Solution**

This project demonstrates a **mature, production-grade approach** to Kubernetes observability:

### **Core Principles:**

1. **🔍 Observe First, Act Second**
   - Continuous monitoring without blind automation
   - Intelligent issue detection with severity classification
   - Structured logging for trend analysis

2. **🛡️ Safety By Design**
   - Non-destructive operations by default
   - Human-readable decision explanations
   - Transparent, debuggable logic

3. **☸️ Cloud-Native Architecture**
   - Runs as a Kubernetes Deployment
   - Uses cluster DNS (no external dependencies)
   - RBAC-secured with least-privilege access

4. **📊 Production-Grade Observability**
   - Real-time metric collection from Prometheus
   - Decision engine with explainable rules
   - Audit trail for all evaluations

---

## 🏗️ **Architecture**
```
┌────────────────────────────────────────────────────────┐
│              Kubernetes Cluster (In-Cluster)           │
│                                                         │
│   ┌──────────────┐         ┌─────────────────┐        │
│   │  Workload    │  ────▶  │   Prometheus    │        │
│   │    Pods      │  Metrics│  (Monitoring)   │        │
│   │              │         └─────────────────┘        │
│   └──────────────┘                  │                  │
│          │                           │                  │
│          │                           ▼                  │
│          │              ┌─────────────────────────┐    │
│          │              │   DevOps Agent (Pod)    │    │
│          │              │                         │    │
│          │              │  ┌──────────────────┐  │    │
│          │              │  │ Metrics Collector│  │    │
│          │              │  │  (Prometheus API)│  │    │
│          │              │  └──────────────────┘  │    │
│          │              │           │             │    │
│          │              │           ▼             │    │
│          │              │  ┌──────────────────┐  │    │
│          │              │  │ Decision Engine  │  │    │
│          │              │  │ (Rule-Based)     │  │    │
│          │              │  └──────────────────┘  │    │
│          │              │           │             │    │
│          │              │           ▼             │    │
│          │              │  ┌──────────────────┐  │    │
│          │              │  │  Action Handler  │  │    │
│          │              │  │ (Safe Logging)   │  │    │
│          │              │  └──────────────────┘  │    │
│          │              │                         │    │
│          │              └─────────────────────────┘    │
│          │                                              │
│          └──────────────────────────────────────────── │
│                     (Monitors itself too!)             │
└────────────────────────────────────────────────────────┘
```

### **Key Design Decisions:**

✅ **In-Cluster Deployment** - Agent runs as a pod inside the cluster  
✅ **Service Discovery** - Uses Kubernetes DNS (`prometheus.svc.cluster.local`)  
✅ **No External Dependencies** - Works without port-forwarding or tunnels  
✅ **RBAC-Compliant** - Least-privilege ServiceAccount  
✅ **Self-Monitoring** - Agent monitors its own health  
✅ **Stateless** - Can be restarted anytime without data loss  

---

## 📁 **Project Structure**
```
AI_assisted_devops/
│
├── agent/
│   ├── main_agent.py          # Core monitoring loop & orchestration
│   ├── metrics_collector.py   # Prometheus API integration
│   ├── decision_engine.py     # Intelligent health analysis
│   ├── action_handler.py      # Safe response & logging
│   └── __init__.py
│
├── config/
│   └── config.yaml            # Thresholds, policies, tuning
│
├── k8s/
│   ├── deployment.yaml        # Agent deployment manifest
│   └── serviceaccount.yaml    # RBAC permissions & roles
│
├── tests/
│   └── test_decision_engine.py # Unit tests
│
├── Dockerfile                 # Multi-stage container build
├── requirements.txt           # Python dependencies
├── run.sh                     # Local development helper
├── .gitignore
├── .env.example              # Environment template
└── README.md                  # This file
```

---

## 🔍 **What Does the Agent Monitor?**

The agent queries Prometheus for **core SRE signals**:

| Metric | Purpose | Threshold |
|--------|---------|-----------|
| **CPU Usage** | Detect resource saturation | >80% |
| **Memory Usage** | Identify memory pressure | >4 GB |
| **Pod Restart Count** | Catch crash loops | >50 restarts |
| **Container Health** | Track liveness/readiness | Health checks |

These metrics are industry-standard indicators used in production Kubernetes monitoring.

---

## 🧠 **Decision Engine: How It Works**

### **Philosophy: Transparent, Explainable Decisions**

The agent uses a **rule-based decision engine** that prioritizes:
- 🔍 **Clarity** - Every decision is logged with reasoning
- 🛡️ **Safety** - Conservative thresholds prevent false positives
- 📊 **Observability** - Structured output for trend analysis

### **Example Decision Flow:**
```python
# Collect metrics
cpu_usage = prometheus.query("container_cpu_usage")
restarts = prometheus.query("kube_pod_restarts")

# Evaluate
if cpu_usage > 80:
    status = "ISSUE"
    severity = "MEDIUM"
    reason = "CPU usage exceeds threshold (80%)"
    
elif restarts > 50:
    status = "ISSUE"
    severity = "HIGH"
    reason = "Pod restart count exceeds safe limit"
    
else:
    status = "NORMAL"
    severity = "LOW"
    reason = "All metrics within operational range"

# Log decision
log_decision(pod_name, status, severity, reason)
```

### **Decision Output Format:**
```json
{
  "timestamp": "2025-01-06T15:23:45Z",
  "pod": "nginx-deployment-7d64c8b9f-x7k2m",
  "status": "ISSUE",
  "severity": "MEDIUM",
  "reason": "CPU usage exceeds threshold (87%)",
  "metrics": {
    "cpu": 87.3,
    "memory": 512.4,
    "restarts": 0
  }
}
```

---

## 🛡️ **Safety-First Design Philosophy**

### **Why Observation Over Automation?**

This project intentionally **does not** implement blind auto-remediation. Here's why:

| Approach | Risk | Production Reality |
|----------|------|-------------------|
| **Blind Auto-Healing** | High | Can cause cascading failures |
| **Observation First** | Low | Safe, debuggable, auditable |
| **Controlled Automation** | Medium | Requires extensive testing & guardrails |

**Industry Truth:** The most respected SRE teams at Google, Netflix, and Amazon emphasize **observability before automation**.

### **Current Behavior (Safe):**
✅ Detects anomalies  
✅ Classifies severity  
✅ Logs structured data  
✅ Provides human-readable insights  

### **Future Enhancement (With Guardrails):**
- Controlled pod restarts with cooldown
- Conservative scaling within strict limits
- Rate-limited actions to prevent automation storms
- Manual approval gates for high-risk operations

**This progression demonstrates production-grade engineering thinking.**

---

## 🚀 **Getting Started**

### **Prerequisites**
- Kubernetes cluster (Minikube, Kind, GKE, EKS, AKS)
- Docker installed
- Helm 3+
- kubectl configured
- Python 3.9+ (for local development)

---

### **Installation**

#### **1️⃣ Start Kubernetes Cluster**
```bash
# Using Minikube
minikube start --cpus=2 --memory=4096
```

#### **2️⃣ Install Prometheus**
```bash
# Add Prometheus Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install Prometheus stack
helm install prometheus prometheus-community/kube-prometheus-stack

# Verify installation
kubectl get pods -n default | grep prometheus
```

#### **3️⃣ Build & Deploy Agent**

**Local Development:**
```bash
# Port-forward Prometheus (for local testing)
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 &

# Run agent locally
python3 agent/main_agent.py
```

**Production Deployment:**
```bash
# Build Docker image
docker build -t ai-devops-agent:v1 .

# Load into Minikube (if using Minikube)
minikube image load ai-devops-agent:v1

# Deploy to cluster
kubectl apply -f k8s/serviceaccount.yaml
kubectl apply -f k8s/deployment.yaml

# Verify deployment
kubectl get pods -l app=ai-devops-agent
```

#### **4️⃣ Watch Agent Logs**
```bash
kubectl logs -f deployment/ai-devops-agent
```

**Expected Output:**
```
🤖 DevOps Agent Started
=========================================
📊 Prometheus: Connected (prometheus-kube-prometheus-prometheus.default.svc.cluster.local)
🔧 Mode: In-Cluster
🛡️  Safety: Observation-Only

🔄 Monitoring Cycle #1
--------------------------------------------
📦 Monitoring 12 pods in namespace: default

Pod: nginx-deployment-7d64c8b9f-x7k2m
  CPU: 23.4% | Memory: 145.2 MB | Restarts: 0
  Status: NORMAL ✅

Pod: redis-master-0
  CPU: 87.6% | Memory: 512.8 MB | Restarts: 0
  Status: ISSUE ⚠️
  Severity: MEDIUM
  Reason: CPU usage exceeds threshold (80%)

⏳ Sleeping 60 seconds before next cycle...
```

---

## ✅ **Verification: Is It Working?**

### **Test 1: Check Agent is Running in Cluster**
```bash
kubectl get pods -l app=ai-devops-agent

# Should show:
# ai-devops-agent-xxxxxxxxxx-xxxxx   1/1   Running   0   2m
```

### **Test 2: Verify In-Cluster Networking**
```bash
# Stop port-forwarding (if running)
# Agent should STILL work (uses Kubernetes DNS)

kubectl logs deployment/ai-devops-agent | grep "Prometheus: Connected"
```

### **Test 3: Trigger Issue Detection**
```bash
# Delete a pod to trigger restarts
kubectl delete pod 

# Watch agent detect the restart spike
kubectl logs -f deployment/ai-devops-agent
```

You should see:
```
Pod: my-app-xxx
  Restarts: 5
  Status: ISSUE ⚠️
  Severity: HIGH
  Reason: Pod restart count exceeds safe limit (50)
```

---

## 🧪 **Live Testing Scenarios**

### **Scenario 1: Simulate High CPU**
```bash
# Deploy CPU stress
kubectl create deployment stress --image=polinux/stress --replicas=1 \
  -- stress --cpu 2 --timeout 120s

# Watch agent logs
kubectl logs -f deployment/ai-devops-agent

# You'll see HIGH CPU detection
```

### **Scenario 2: Simulate Crash Loop**
```bash
# Create a pod that crashes repeatedly
kubectl run crasher --image=busybox --restart=Always \
  -- sh -c "sleep 5; exit 1"

# After 3-4 minutes, agent will detect restart anomaly
```

### **Scenario 3: Agent Self-Monitoring**
```bash
# Delete the agent itself
kubectl delete pod -l app=ai-devops-agent

# Kubernetes recreates it automatically
# Agent resumes monitoring seamlessly (stateless design)
```

---

## 📊 **Understanding the Output**

### **Log Structure**
```json
{
  "cycle": 42,
  "timestamp": "2025-01-06T15:23:45Z",
  "namespace": "default",
  "total_pods": 12,
  "issues_detected": 2,
  "evaluations": [
    {
      "pod": "nginx-7d64c8b9f-x7k2m",
      "status": "ISSUE",
      "severity": "MEDIUM",
      "reason": "CPU usage exceeds threshold (87%)",
      "metrics": {
        "cpu": 87.3,
        "memory": 145.2,
        "restarts": 0
      }
    }
  ]
}
```

### **Severity Levels**
- **LOW** - Normal operation
- **MEDIUM** - Elevated metrics, trending toward threshold
- **HIGH** - Critical threshold exceeded, immediate attention needed

---

## 🎯 **Skills Demonstrated**

This project showcases production-grade DevOps capabilities:

### **Kubernetes Expertise**
✅ Pod lifecycle management  
✅ Deployments & ReplicaSets  
✅ RBAC (ServiceAccounts, Roles, RoleBindings)  
✅ Service discovery & DNS  
✅ In-cluster networking  
✅ Container best practices  

### **Observability & Monitoring**
✅ Prometheus integration  
✅ PromQL queries  
✅ Metric collection & analysis  
✅ Structured logging  
✅ Time-series data interpretation  

### **System Design**
✅ Safety-first architecture  
✅ Stateless application design  
✅ Graceful error handling  
✅ Production debugging mindset  

### **DevOps Philosophy**
✅ Observation before automation  
✅ Explainable decision-making  
✅ Audit trails & transparency  
✅ Conservative operational practices  

---

## 🔮 **Roadmap: Future Enhancements**

### **Phase 1: Controlled Automation** (Next iteration)
- [ ] Pod restart with 15-minute cooldown
- [ ] Conservative scaling (±1 replica only)
- [ ] Rate limiting (max 5 actions/hour)
- [ ] Dry-run mode for testing

### **Phase 2: Advanced Analysis**
- [ ] Trend detection (CPU increasing over time)
- [ ] Correlation analysis (CPU + Memory patterns)
- [ ] Historical baseline comparison
- [ ] Anomaly scoring

### **Phase 3: Integrations**
- [ ] Slack notifications for high-severity issues
- [ ] PagerDuty integration
- [ ] Grafana dashboard
- [ ] Webhook support for custom integrations

### **Phase 4: AI Enhancement**
- [ ] LLM-based root cause analysis
- [ ] Natural language incident summaries
- [ ] Contextual recommendations
- [ ] Predictive issue detection

**Important:** Each phase will maintain the core safety-first principle.

---

## 🛡️ **Security & RBAC**

### **ServiceAccount Permissions (Least Privilege)**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ai-agent-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]  # Read-only
- apiGroups: [""]
  resources: ["pods/status"]
  verbs: ["get"]  # Status only
```

**Key Security Features:**
- ✅ No write permissions in current version
- ✅ No access to secrets or configmaps
- ✅ Namespace-scoped (can be cluster-scoped if needed)
- ✅ No privileged containers
- ✅ Runs as non-root user

---

## 🤝 **Contributing**

Contributions are welcome! This project follows standard Git workflow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

**Please ensure:**
- Code follows PEP 8 style guide
- New features include tests
- Documentation is updated
- Safety principles are maintained

---

## 👤 **Author**

**M Brinesh Varshan**  
DevOps Engineer | Kubernetes | Cloud Infrastructure | Observability

- 📧 Email: brineshvarshan28@gmail.com

---

## 🙏 **Acknowledgments**

- **Kubernetes Community** - For excellent documentation and tools
- **Prometheus** - For reliable metrics infrastructure
- **Google SRE Book** - For observability best practices
- **CNCF** - For cloud-native ecosystem

---

## 📚 **Learn More**

### **Related Reading:**
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [Kubernetes Monitoring Guide](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/naming/)

### **Similar Projects:**
- [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
- [prometheus-operator](https://github.com/prometheus-operator/prometheus-operator)

---

<p align="center">
  <strong>⭐ If this project helped you, please star the repository! ⭐</strong>
</p>

<p align="center">
  <em>Built with production-grade thinking, safety-first design, and Kubernetes best practices</em>
</p>

<p align="center">
  <strong>Not just automation—intelligent observability.</strong>
</p>

---

## 📌 **Project Tags**

`kubernetes` `devops` `prometheus` `monitoring` `observability` `sre` `site-reliability-engineering` `python` `docker` `cloud-native` `infrastructure` `production-grade` `safety-first` `decision-engine` `metrics` `alerting`
```

---

## 🔥 **KEY IMPROVEMENTS IN THIS VERSION:**

### **1. Accurately Reflects Your Project**
- ✅ Emphasizes observation over blind automation
- ✅ Explains WHY this approach is mature
- ✅ Shows production-grade thinking

### **2. Professional Positioning**
- ✅ "Safety-first" is a STRENGTH, not a limitation
- ✅ Compares to industry practices (Google, Netflix)
- ✅ Shows you understand real production concerns

### **3. Interview-Ready Explanations**
- ✅ Clear decision flow
- ✅ Safety justifications
- ✅ Future enhancement roadmap

### **4. Production Credibility**
- ✅ RBAC details
- ✅ Security considerations
- ✅ Testing scenarios
- ✅ Verification steps

---


Tech Stack: Python, Kubernetes, Prometheus, Docker, PromQL, RBAC, Cloud-Native Architecture
