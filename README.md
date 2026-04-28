🚀 DE Training Lab: Modern Kafka (KRaft) Setup
This project uses Kafka KRaft Mode, which removes the need for ZooKeeper. It’s faster, simpler, and follows the latest architectural standards.  

🛠 Quick Start
Launch Stack: docker-compose up -d

Setup Python: pip install -r python_app/requirements.txt

🏗 Training Modules
1. Manage Topics
Since we aren't using ZooKeeper, we interact directly with the Kafka broker.

Bash
# Create a topic
docker exec kafka kafka-topics --create --topic training_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# List topics
docker exec kafka kafka-topics --list --bootstrap-server localhost:9092
2. Data Flow
Run python python_app/producer.py to start sending mock sensor data.

Run python python_app/consumer.py in a separate terminal to watch the data flow from Kafka into MongoDB.

3. Exploration
Open MongoDB Compass (or a CLI) and check the training_db database.

Go to Prometheus (localhost:9090) to see if the Kafka broker is healthy.

Note: If the Python app is running inside a Docker container, change localhost:9092 to kafka:9092 in your connection strings!