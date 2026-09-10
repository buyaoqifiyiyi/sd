@echo off
cd /d "%~dp0web"
start "SD Film Web" /b node server.mjs
start "" http://127.0.0.1:4173
