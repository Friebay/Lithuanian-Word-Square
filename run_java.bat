@echo off
echo Compiling App.java...
javac -g:none -nowarn -encoding UTF-8 App.java

if %errorlevel% neq 0 (
    echo Compilation failed.
    pause
    exit /b %errorlevel%
)

echo Compilation successful.
echo Running App...

REM Run and save output to log.txt (overwrite each time)
java -server -Xms2g -Xmx8g -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:+UseStringDeduplication -XX:+TieredCompilation -XX:MaxInlineSize=1024 -XX:+AlwaysPreTouch -XX:+PerfDisableSharedMem -XX:+DisableExplicitGC -XX:+UseCompressedOops App > log.txt

echo.
echo Program finished. Log saved to log.txt
pause
