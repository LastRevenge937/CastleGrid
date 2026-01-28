class Sentinel:
    def __init__(self, grid):
        self.grid = grid

    def firewall_alert(self, layer_index: int, message: str):
        self.grid.log_firewall_event(
            f"Layer {layer_index}: {message}"
        )

    def firewall_status_report(self):
        report = []
        if self.grid.global_firewall:
            report.append(
                f"GLOBAL: {self.grid.global_firewall.name} (ONLINE)"
            )
        for layer in self.grid.layers:
            if layer.firewall:
                report.append(
                    f"Layer {layer.index}: {layer.firewall.name} ({layer.firewall_status})"
                )
        return report
