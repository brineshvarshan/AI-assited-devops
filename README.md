# AI-assited-devops
🤖 AI-Assisted Kubernetes Monitoring & Decision Agent








A Kubernetes-native DevOps agent that runs inside the cluster, continuously monitors infrastructure using Prometheus, analyzes system health using a decision engine, and safely reacts to operational issues.

This project focuses on real-world DevOps fundamentals:
monitoring, decision-making, safety, containerization, and Kubernetes internals.

🎯 Why This Project?

In real Kubernetes environments:

Manual monitoring does not scale

Engineers detect problems after incidents occur

Alert fatigue hides real issues

Blind auto-healing can be dangerous

This project demonstrates how to build a safe, observable, in-cluster monitoring agent that:

Detects problems early

Makes decisions programmatically

Avoids unsafe automation

Runs fully inside Kubernetes

🧠 What Does the Agent Do?

Every few seconds, the agent:

Collects cluster metrics from Prometheus

Evaluates metrics using a decision engine

Detects abnormal behavior (CPU, memory, restarts)

Logs issues with severity classification

Runs continuously as a Kubernetes Deployment

The current version is observation-first (safe by design).
Auto-remediation can be added later.

🏗️ Architecture (Actual Implementation)
┌──────────────────────────────────────────────┐
│              Kubernetes Cluster              │
│                                              │
│  ┌────────────┐      ┌──────────────┐       │
│  │ Workload   │ ---> │ Prometheus   │       │
│  │   Pods     │      │  (Metrics)   │       │
│  └────────────┘      └──────────────┘       │
│          │                    │               │
│          │                    ▼               │
│          │        ┌────────────────────┐     │
│          │        │ DevOps Agent (Pod) │     │
│          │        │                    │     │
│          │        │ • Metrics Collector│     │
│          │        │ • Decision Engine  │     │
│          │        │ • Action Handler   │     │
│          │        └────────────────────┘     │
│                                              │
└──────────────────────────────────────────────┘

Key Design Choices

Runs inside the cluster

Uses Kubernetes DNS (*.svc.cluster.local)

No localhost dependencies in production

RBAC-secured ServiceAccount

Safe, non-destructive actions by default

📁 Project Structure
AI_assisted_devops/
│
├── agent/
│   ├── main_agent.py          # Agent loop & orchestration
│   ├── metrics_collector.py   # Prometheus queries
│   ├── decision_engine.py     # Health analysis logic
│   ├── action_handler.py      # Safe response handling
│
├── config/
│   └── config.yaml            # Thresholds & tuning
│
├── k8s/
│   ├── deployment.yaml        # Agent deployment
│   └── serviceaccount.yaml   # RBAC permissions
│
├── Dockerfile
├── requirements.txt
├── run.sh                     # Local execution helper
├── .gitignore
└── README.md

📊 Metrics Monitored

The agent queries Prometheus for:

CPU usage

Memory usage

Pod restart count

These are core SRE signals used in production monitoring systems.

🧠 Decision Engine (How Decisions Are Made)

The decision engine evaluates metrics using clear, explainable rules.

Example:

CPU usage > threshold → issue

Memory usage > threshold → issue

Pod restarts > threshold → issue

Each evaluation produces:

Status (NORMAL / ISSUE)

Severity (low, medium)

Reason (human-readable)

This keeps decisions transparent and debuggable.

🛡️ Safety-First Design

⚠️ This project intentionally avoids blind automation.

Current behavior:

Detects problems

Logs structured output

Allows humans to observe trends

Why?

In production, safety > speed

Automation should be earned, not assumed

🐳 Running the Project
Local (Development)
python3 agent/main_agent.py


Prometheus is accessed using port-forwarding during local testing.

Inside Kubernetes (Production-Style)
docker build -t ai-devops-agent:v1 .
minikube image load ai-devops-agent:v1
kubectl apply -f k8s/


Watch logs:

kubectl logs -f deployment/ai-devops-agent

✅ How to Verify It’s Running Inside the Cluster

Agent runs as a Pod

Uses Kubernetes service DNS (not localhost)

Continues working without port-forwarding

Survives pod restarts

Reacts to pod crashes and restarts

🧪 Live Test
kubectl delete pod <any-non-system-pod>
kubectl logs -f deployment/ai-devops-agent


You will see:

Restart count increase

Issue detected

Decision logged

🎯 Skills Demonstrated

Kubernetes (Pods, Deployments, RBAC)

Prometheus & PromQL

Docker & container lifecycle

In-cluster networking

Monitoring & observability principles

Safe automation design

Real debugging & production thinking

🚀 Future Enhancements (Planned)

Controlled auto-remediation (restart / scale)

Cooldown & rate-limiting logic

Alerting (Slack / Email)

AI-assisted root cause suggestions

Multi-namespace monitoring

👤 Author

M Brinesh Varshan
DevOps Engineer | Kubernetes | Cloud | Security

⭐ Final Note

This project focuses on doing things correctly, not just automatically.

It demonstrates:

How monitoring actually works

How decisions are made

Why safety matters in DevOps

How real Kubernetes systems behave

Built to understand, not just to impress.