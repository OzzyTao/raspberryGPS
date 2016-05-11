#! /bin/bash
# /etc/init.d/GPSdaemon
#
### BEGIN INIT INFO
# Provides: GPSdaemon
# Required-Start: 
# Should-Start: 
# Required-Stop: 
# Should-Stop:
### END INIT INFO

# Activate the python virtual environment
    . /path_to_virtualenv/activate

case "$1" in
  start)
    echo "Starting server"
    # Start the daemon 
    python /usr/share/testdaemon/testdaemon.py start
    ;;
  stop)
    echo "Stopping server"
    # Stop the daemon
    python /usr/share/testdaemon/testdaemon.py stop
    ;;
  restart)
    echo "Restarting server"
    python /usr/share/testdaemon/testdaemon.py restart
    ;;
  *)
    # Refuse to do other stuff
    echo "Usage: /etc/init.d/testdaemon.sh {start|stop|restart}"
    exit 1
    ;;
esac

exit 0