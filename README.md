# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 326
- HTTP: 356 alive / 36 gold
- HTTPS: 223 alive / 10 gold
- SOCKS4: 220 alive / 149 gold
- SOCKS5: 230 alive / 131 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14139
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
