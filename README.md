# Linux Server Storage Data Collector

The Linux Server Storage Data Collector is a Bash script that collects storage-related data from a Linux server using various commands. It then converts this data into a CSV format and inserts it into a remote MySQL database. This project utilizes the Paramiko module for SSH connectivity.

## Table of Contents

- [Linux Server Storage Data Collector](#linux-server-storage-data-collector)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)


## Introduction

This Bash script is designed to automate the collection and storage of storage-related data from a Linux server. It's particularly useful for system administrators and DevOps engineers who need to monitor and manage server storage.

## Features

- Collects data on filesystems, including size, usage, and availability.
- Gathers information on disk usage by mounted paths.
- Retrieves system and network information.
- Converts collected data into a CSV format.
- Inserts CSV data into a remote MySQL database.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Windows system for running this project.
- A remote Linux server with SSH access.
- MySQL database access on a remote server.
- Paramiko Python module (used for SSH communication).

## Installation

1. Clone this repository to your local machine.


2. Install the Paramiko Python module if not already installed.


## Usage

1. Configure the script by editing the `mylinux.json` file. Provide SSH connection details, Linux commands to gather data, and MySQL database credentials.

2. Run the script by executing the `main.py` script.
3. The script will collect data, convert it into CSV format, and insert it into the remote MySQL database.

## Configuration

In the `database.py` file, you can specify the following configurations:

- SSH connection details: Hostname, username, and password.
- Linux commands to collect data.
- MySQL database credentials.
- Output file paths for CSV data.
