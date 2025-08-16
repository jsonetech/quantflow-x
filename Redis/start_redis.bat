@echo off
echo Starting Redis for QuantFlow X 2.0...
cd /d "a:\Desarrollos\quantflow-x\MCP\Redis\redis"
"a:\Desarrollos\quantflow-x\MCP\Redis\redis\redis-server.exe" "a:\Desarrollos\quantflow-x\MCP\Redis\redis\redis.conf"
pause
