class EscortAgent:
    """
    Simulated agent that 'escorts' files from source to destination
    Marks as encrypted but keeps safe and read-only
    """
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def escort(self, grid_file, source, destination):
        grid_file.log(f"Escorted by Agent {self.agent_id}")
        grid_file.log(f"{source} → {destination} (encrypted)")
