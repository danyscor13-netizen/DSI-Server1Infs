from cloudlink import server
from cloudlink.server.protocols import clpv4

# Create the server
srv = server()

# Logging
srv.logging.basicConfig(
    level=srv.logging.INFO
)

# Enable CloudLink Protocol v4
clpv4 = clpv4(srv)

# Start the server
srv.run(
    ip="0.0.0.0",
    port=3000
)
