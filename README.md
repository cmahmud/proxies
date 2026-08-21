# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 408
- HTTP: 286 alive / 100 gold
- HTTPS: 204 alive / 30 gold
- SOCKS4: 222 alive / 156 gold
- SOCKS5: 233 alive / 122 gold

## Historical pool

- Discovered: 160287
- Ever alive: 30810
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
