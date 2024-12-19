from pydantic_ai import Agent
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()

agent = Agent(
    'gemini-1.5-flash',
    system_prompt='Be concise, reply with one sentence.',
)

result = agent.run_sync('Give me the job description of an AI engineer')
print(result.data)
