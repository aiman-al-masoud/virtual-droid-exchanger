# Setup

## On your Host Machine

1. Clone this repository

```bash
git clone link-from-github
```

2. Directories...

3. Run the Python server 

```bash
cd server
python3 app.py
```

## On your Android VM

1. Install Termux on your Android VM

2. Fire up Termux and install the following dependencies:

```bash
pkg install git
pkg install wget
pkg install zip
```

3. Clone this repository

```bash
git clone link-from-github
```

4. Edit client.sh and make sure the directories `get-from-host` and  `push-to-host` exist.

5. Run the client script

```
chmod +x client.sh
./client.sh
```

You're ready 