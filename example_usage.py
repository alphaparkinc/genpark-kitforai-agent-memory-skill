from client import KitForAiAgentMemoryClient
client = KitForAiAgentMemoryClient()
db = [{"content": "User likes coffee", "relevance": 0.9}, {"content": "Launch happened yesterday", "relevance": 0.4}]
print(client.recall_memories("does user want coffee?", db))