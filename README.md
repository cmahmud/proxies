# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 416
- HTTP: 203 alive / 83 gold
- HTTPS: 147 alive / 23 gold
- SOCKS4: 202 alive / 150 gold
- SOCKS5: 216 alive / 160 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27405
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
