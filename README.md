# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 409
- HTTP: 273 alive / 86 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 240 alive / 152 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 166318
- Ever alive: 32383
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
