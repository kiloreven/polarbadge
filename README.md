# polarbadge

## requirements

- libpango
- ghostscript
- poppler-utils

Fedora prep:

``` bash
sudo dnf install -y pango-devel ghostscript poppler-utils
```

## quickstart

``` bash
uv sync
cp config.toml.example config.toml
uv run ./cli.py pp33-everyone
# or
uv run ./cli.py pp33-user -u 1234
```
