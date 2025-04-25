@echo off
echo Pushing to GitHub...
git add .
git commit -m "Auto push"
git push
echo.
echo ---------------------------
echo Done! Opening Render...
start https://dashboard.render.com/web/srv-d05cdf3uibrs73fiua4g/deploys
echo ---------------------------
pause
