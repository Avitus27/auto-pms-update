# Auto PMS Update

## Setup and Run
```bash
$ cp .env.example .env
$ pip install -r requirements.txt
$ ./main.py
> or
$ python3 main.py
```

## Settings

Settings are saved in the `.env` file created during the setup described above

### OS
Valid values:
- Windows
- MacOS
- Linux
- FreeBSD

### Build
Specific value depends on OS and platform.
Valid values:
- windows-x86
- darwin-x86_64
- linux-x86
- linux-x86_64
- linux-aarch64
- linux-armv7hf_neon
- freebsd-x86_64

### Plex Location
The location of the Plex Media Server executable. Test this value is valid by running `$ /path/to/exec/Plex\ Media\ Server --version`.

### Download Location
Where you want the file saved. Just make sure the path is valid.
