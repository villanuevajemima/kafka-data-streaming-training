📊 Reference Dataset
Source: E-commerce Clickstream and Transaction Dataset (Kaggle)

Why: It contains fields like UserID, SessionID, Timestamp, and EventType. This allows trainees to simulate a "live" store where data never stops.

📋 Business Requirement Document (BRD)
Project Title: Project "Falcon" – Real-Time User Behavior Analytics

Stakeholder: VP of Data Operations (Gemini AI)

Status: Draft / For Review

1. Executive Summary
Our marketing department is losing money because we only analyze customer behavior 24 hours after it happens. We need a "Live Analytics" engine that captures user interactions the moment they occur.

2. Business Objectives
Latency: Data must be available for querying in MongoDB within 5 seconds of the event.

Data Integrity: The system must handle "Dirty Data" without crashing the entire pipeline.

Scalability: The architecture must use a modern, ZooKeeper-less Kafka (KRaft) setup to ensure we are ready for cloud migration.

Real-Time Ingestion:
A Python producer must stream the Kaggle dataset into a Kafka topic user_clicks.

Deduplication:
The consumer must identify and ignore duplicate SessionID + Timestamp entries.

Schema Validation:
"Bad data" (e.g., missing UserID or negative Amount) must be redirected to a "Dead Letter" collection in Mongo.

Observability:
A Grafana dashboard showing "Events per Second" and "Error Rate."

🏗 The Mini-Project Design
Phase 1: Infrastructure (The "Skeleton")
Trainees must use the KRaft Docker Compose provided previously.

Task: Spin up Kafka, MongoDB, and Grafana.

Validation: Use docker exec to create the topic user_clicks manually before starting the app.

Phase 2: The "Chaos" Producer
Trainees will write a Python script that reads the Kaggle CSV and pushes it to Kafka. To simulate real-world pain, they must programmatically inject:

Duplicates: Every 10th message should be sent twice.

Bad Data: Every 20th message should have the EventType set to NULL or a string of gibberish.

Phase 3: The "Intelligent" ConsumerThe consumer shouldn't just "dump" data. It must:Check for Duplicates: Use a Redis cache or a quick Mongo lookup to see if the event exists.Validate: * If valid $\rightarrow$ Save to events collection.If invalid $\rightarrow$ Save to error_logs collection for debugging.

Phase 4: Monitoring (The "Eyes")
Metric: Count successful vs. failed inserts.

Goal: Build a Grafana panel that shows a red alert if the "Bad Data" rate exceeds 5%.