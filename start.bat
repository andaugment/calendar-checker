@echo off
chcp 65001 > nul
echo Starting calendar checker...
start /b python -m http.server 8080
timeout /t 2 /nobreak > nul
start http://localhost:8080
echo.
echo Browser opened. Close this window to stop the server.
pause > nul
