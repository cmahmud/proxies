# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 326
- HTTP: 376 alive / 37 gold
- HTTPS: 224 alive / 10 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 227 alive / 131 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14137
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
