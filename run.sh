#!/bin/bash

# Raspkei run script template
# Usage: ./run.sh <command> [args]
# Example: ./run.sh apache
#          ./run.sh hotspot
#          ./run.sh battery

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PY_DIR="$PROJECT_DIR/py"

function usage() {
    echo -e "\nRASPKEI PROJECT"
    echo -e "\nUsage: $0 <command> [args]\n"
    echo "Commands:"
    echo "  help          Displays this message, commands, etc.."
    echo -e "\n"
    echo "  apache        Installs Apache (py/runapache.py)"
    echo "  resetapache   Remove Apache (py/resetapache.py)"
    echo -e "\n"
    echo "  hotspot       Init. WiFi Hotspot (py/runhotspot.py)"
    echo "  checkhotspot  Check Hotspot Status (py/checkhotspot.py)"
    echo -e "\n"
    echo "  battery       Battery Stats. Script (py/batt.py)"
    echo "  batt_stats    Webserver Battery Stats. (py/batt_stats.py)"
    echo "  movehtml      Move web files to /var/www/html (py/movehtml.py)"
    exit 1
}

function safe_run() {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "Error: Command failed: $*" >&2
        exit $status
    fi
}

if [ $# -lt 1 ]; then
    usage
fi

COMMAND="$1"
shift

case "$COMMAND" in
    apache)
        safe_run python3 "$PY_DIR/runapache.py" "$@"
        ;;
    hotspot)
        safe_run python3 "$PY_DIR/runhotspot.py" "$@"
        ;;
    battery)
        safe_run python3 "$PY_DIR/batt.py" "$@"
        ;;
    checkhotspot)
        safe_run python3 "$PY_DIR/checkhotspot.py" "$@"
        ;;
    resetapache)
        safe_run python3 "$PY_DIR/resetapache.py" "$@"
        ;;
    batt_stats)
        safe_run python3 "$PY_DIR/batt_stats.py" "$@"
        ;;
    movehtml)
        safe_run sudo python3 "$PY_DIR/movehtml.py" "$@"
        ;;
    help|--help|-h)
        usage
        ;;
    *)
        echo "Unknown command: $COMMAND"
        usage
        ;;
esac

exit 0