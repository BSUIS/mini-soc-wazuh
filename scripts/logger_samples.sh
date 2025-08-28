#!/bin/bash

# Simulate SSH failed logins
logger -p auth.info "sshd[12345]: Failed password for testuser from 192.168.1.100 port 54321 ssh2"
sleep 1
logger -p auth.info "sshd[12346]: Failed password for testuser from 192.168.1.100 port 54322 ssh2"
sleep 1
logger -p auth.info "sshd[12347]: Failed password for testuser from 192.168.1.100 port 54323 ssh2"
sleep 2

# Simulate successful login
logger -p auth.info "sshd[12348]: Accepted password for newuser from 192.168.1.100 port 54324 ssh2"

echo "Test logs sent to syslog"
