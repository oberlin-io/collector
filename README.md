## Linux nstall requirements
- sysstat
- rsyslog

rsyslog as a log daemon, as Stretch doesn't seem to have syslog and auth.log files.

## Changes
- Use ```meta.yaml``` for configuration and variables.
- The ```filelines``` module replaces ```filewatch``` function, plus returning new lines.
I had thought a mod time check would use less memory, require less work.
But th elog files are constantly being updated, so might as well run through all the lines.
