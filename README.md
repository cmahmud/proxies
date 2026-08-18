# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 300
- HTTP: 424 alive / 30 gold
- HTTPS: 252 alive / 5 gold
- SOCKS4: 226 alive / 139 gold
- SOCKS5: 216 alive / 126 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13405
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
