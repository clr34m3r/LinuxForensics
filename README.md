<h1 align="center">Linux Forensics</h1>

The Linux forensics tool project provides a toolkit that collects the evidence from all PCs 🖥️, using Linux operating system. The gathered evidence includes System Data, Network Data, Event Data, User Data.

## System Data
- Collect system information
- Collect list of open files
- Collect process status
- Collect disk filesystems information
- Collect list of mounted filesystems
- Collect loaded kernel modules information
- Collect file metadata
- Collect file hashes

## Network Data
- Collect network interfaces
- Collect network statistics
- Collect network routing tables

## Event Data
- Collect list of last logged-in users
- Collect list of failed logins
- Collect bash history
- Collect log files
- Collect browser history

## User Data
- Collect local users information
- Check the integrity of local user credentials

## Ensure the integrity of the evidence collected
- Compress files, export encrypted SHA256 signature for integrity check
