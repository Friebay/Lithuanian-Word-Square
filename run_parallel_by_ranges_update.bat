@echo off
setlocal

rem 1. Define the path to Java 25 (using short name/quotes to be safe)
set "JAVA25=C:\Users\zabit\AppData\Local\Programs\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\java.exe"

rem 2. Optimized JVM options for Java 25
set JVM_OPTS=-Xms2g -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:+UseCompressedOops

rem 3. Launching
rem We use "set var=" inside the cmd /c to ensure the sub-process is clean.
rem We also use the older -Xlog syntax style which is more compatible with shell quoting.

echo Launching Core 1...
start "core1" /affinity 1 cmd /c "set _JAVA_OPTIONS=&& set JAVA_TOOL_OPTIONS=&& set JDK_JAVA_OPTIONS=&& "%JAVA25%" %JVM_OPTS% -Xlog:gc:file=gc_core1.log -cp . App_Parallelized 0 9 > log_core1.txt 2>&1"

echo Launching Core 2...
start "core2" /affinity 2 cmd /c "set _JAVA_OPTIONS=&& set JAVA_TOOL_OPTIONS=&& set JDK_JAVA_OPTIONS=&& "%JAVA25%" %JVM_OPTS% -Xlog:gc:file=gc_core2.log -cp . App_Parallelized 10 16 > log_core2.txt 2>&1"

echo Launching Core 3...
start "core3" /affinity 4 cmd /c "set _JAVA_OPTIONS=&& set JAVA_TOOL_OPTIONS=&& set JDK_JAVA_OPTIONS=&& "%JAVA25%" %JVM_OPTS% -Xlog:gc:file=gc_core3.log -cp . App_Parallelized 17 23 > log_core3.txt 2>&1"

echo Launching Core 4...
start "core4" /affinity 8 cmd /c "set _JAVA_OPTIONS=&& set JAVA_TOOL_OPTIONS=&& set JDK_JAVA_OPTIONS=&& "%JAVA25%" %JVM_OPTS% -Xlog:gc:file=gc_core4.log -cp . App_Parallelized 24 32 > log_core4.txt 2>&1"

echo All processes started.
pause