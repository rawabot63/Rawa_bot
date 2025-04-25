git add .
git commit -m "auto push"
git push
@echo off
echo ---------------------------
echo Pushing to GitHub & Deploy
echo ---------------------------

cd /d %~dp0

git add .
git commit -m "auto deploy"
git push origin main

echo ---------------------------
echo Done! Check your Render.com
echo ---------------------------
pause
