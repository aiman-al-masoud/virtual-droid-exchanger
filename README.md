# virtual-droid-exchanger

A stupid hack to exchange files between an Android VM and the host OS. (Without using shared folders or ssh).


# Setup

## On your Host Machine

1. Clone this repository

2. Run the Python server 

```bash
cd server/
python3 __main__.py
```

3. Check that the following directories have been created

``` bash
/home/username/Desktop/push-to-droid
bash: /home/username/Desktop/push-to-droid: Is a directory
/home/username/Desktop/get-from-droid
bash: /home/username/Desktop/get-from-droid: Is a directory
```

## On your Android VM

1. Install Termux on your Android VM

2. Fire up Termux and install the following dependencies:

``` bash
pkg install git
pkg install wget
pkg install zip
```

3. Clone this repository

4. Run the client script

```bash
cd client/
./start-client.sh
```
5. Check that the following directories have been created

``` bash
/data/data/com.termux/files/home/push-to-host
/data/data/com.termux/files/home/push-to-host: Is a directory
/data/data/com.termux/files/home/get-from-host
/data/data/com.termux/files/home/get-from-host: Is a directory
```
6. Try it out

### Android VM -> Host

On your Android VM, copy a file into `push-to-host/`, then go to your host OS and check that it's been copied to `get-from-droid/`.

### Host -> Android VM

On your host OS, copy a file into `push-to-droid/`, then go to your Android VM and check that it's been copied to `get-from-host`.

## Bonus
To avoid having to run `start-client.sh` on a separate shell session every time you power on your VM, try saving its state. Or adding `start-client.sh` as an <a href="https://wiki.termux.com/wiki/Termux:Boot">"on boot script"</a> in Termux (didn't work out properly for me).




