class KitForAiAgentMemoryClient:
    def recall_memories(self, current_query: str, memory_db: list[dict]) -> dict:
        # Simulated keywords similarity routing
        keywords = set(current_query.lower().split())
        matches = []
        for mem in memory_db:
            content = mem.get("content", "").lower()
            if any(k in content for k in keywords):
                matches.append(mem)
        return {"matched_memories": sorted(matches, key=lambda x: x.get("relevance", 0.0), reverse=True)}