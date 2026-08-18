# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 214
- HTTP: 523 alive / 36 gold
- HTTPS: 226 alive / 10 gold
- SOCKS4: 232 alive / 97 gold
- SOCKS5: 208 alive / 71 gold

## Historical pool

- Discovered: 85902
- Ever alive: 5723
- Ever gold: 287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
