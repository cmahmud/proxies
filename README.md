# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 403
- HTTP: 233 alive / 89 gold
- HTTPS: 175 alive / 22 gold
- SOCKS4: 204 alive / 141 gold
- SOCKS5: 248 alive / 151 gold

## Historical pool

- Discovered: 151946
- Ever alive: 27804
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
