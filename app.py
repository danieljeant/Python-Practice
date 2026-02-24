from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent / "web"), **kwargs)


def run() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8000), DashboardHandler)
    print("Serving Quant dashboard on http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
