# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 393
- HTTP: 200 alive / 71 gold
- HTTPS: 139 alive / 21 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 222 alive / 153 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26025
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
