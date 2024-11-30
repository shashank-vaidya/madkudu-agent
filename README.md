# Madkudu Agent: AI-Powered Autonomous Lead Scoring and Engagement Automation

Madkudu Agent is an AI-driven autonomous system designed to streamline lead scoring and engagement workflows. By leveraging CrewAI agents, this project automates complex tasks such as data preprocessing, predictive analytics, and personalized email generation. The AI agents operate with minimal human intervention, making decisions and executing workflows based on pre-configured goals and logic.

---

## **Autonomous Features**

### **1. AI Agent Collaboration**
- CrewAI agents are orchestrated to perform tasks independently while adhering to their assigned goals.
- Agents collaborate to:
  - Score leads based on engagement metrics.
  - Identify top leads and prioritize actions.
  - Generate and manage personalized email drafts autonomously.

### **2. Decision-Making Capabilities**
- Each agent is programmed with a clear **goal**, **role**, and **backstory** to guide its decision-making process.
- Autonomous tools and workflows enable agents to:
  - Analyze data and extract actionable insights.
  - Use predefined templates and logic to draft tailored emails.

### **3. End-to-End Automation**
- The entire workflow is handled autonomously by agents, from preprocessing raw data to generating actionable insights and drafting communication.

---

## **Key Components**

### **1. CrewAI Agents**

- **Lead Scoring Agent**:
  - Role: To classify leads into categories (`Easy`, `Medium`, `Difficult`) using AI-powered predictions.
  - Goal: Identify leads most likely to convert and prioritize them for action.
  - Backstory: Operates as an analytical expert, assessing engagement metrics.

- **Email Follow-Up Agent**:
  - Role: To autonomously generate personalized follow-up emails for prioritized leads.
  - Goal: Ensure each email aligns with the lead’s engagement level and interests.
  - Backstory: Mimics a sales specialist with expertise in lead engagement.

### **2. Orchestrated Workflows**
- The project employs **CrewAI's hierarchical task orchestration** to ensure agents work together efficiently:
  1. The **Lead Scoring Agent** preprocesses and classifies leads.
  2. The **Email Follow-Up Agent** acts on the top leads and generates tailored communication.

### **3. Adaptive Learning**
- The autonomous agents can be retrained or reconfigured to adapt to changing business requirements, ensuring long-term scalability.

---

## **How It Works**

### **1. Autonomous Workflow**
- CrewAI agents are configured using `agents.yaml` and `tasks.yaml` to act independently.
- The system processes data in the following steps:
  1. **Preprocessing**:
     - Normalizes and encodes engagement metrics.
  2. **Scoring**:
     - Classifies leads into actionable categories using an XGBoost model.
  3. **Communication**:
     - Generates personalized follow-up emails for `Easy` leads, prioritizing those with high engagement scores.

### **2. Engagement Metrics**
- Key metrics analyzed by the agents include:
  - Website visits
  - Time spent on the platform
  - Content downloads
  - Product trials
  - Event attendance

---

## **Upcoming Features**
1. **CRM API Integration**:
   - Automate the input of lead data directly from CRM platform.
   - Features:
     - Real-time syncing of lead engagement metrics.
     - Automatic updates to the scoring pipeline when new leads are added.

2. **Connecting Real Sales Representatives' Email Accounts**:
   - Enable agents to send emails from authenticated sales representatives’ accounts.
   - Benefits:
     - Improves trust and credibility in email communication.
     - Allows personalized follow-ups from actual employee profiles.
   - Implementation:
     - OAuth-based email authentication for platforms like Gmail and Outlook.
     - Store email templates and logs per representative for tracking.

---

## **Installation Instructions**

### **1. Clone the Repository**
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/shashank-vaidya/madkudu-agent.git
```
```bash
cd madkudu-agent
```
### **2. Set Up the Python Environment**
To ensure compatibility and dependency isolation, set up a virtual environment:

For macOS/Linux:
Create the environment:
```bash
python3 -m venv env
```
Activate the environment:
```bash
source env/bin/activate
```
For Windows:
Create the environment:
```bash
python -m venv env
```
Activate the environment:
```bash
env\Scripts\activate
```
3. Install Required Dependencies
Install the necessary Python packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```
4. Configure Environment Variables
This project uses environment variables for secure configuration. Create a .env file in the root directory and include:
```bash
OPENAI_API_KEY=<your_openai_api_key>
```
Replace <your_openai_api_key> with your actual OpenAI API key.

5. Run the Workflow
To execute the full workflow, run the main.py script:

```bash
python main.py
```
