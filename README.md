# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 326
- HTTP: 368 alive / 37 gold
- HTTPS: 216 alive / 10 gold
- SOCKS4: 226 alive / 148 gold
- SOCKS5: 231 alive / 131 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14139
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
