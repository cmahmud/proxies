# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 319
- HTTP: 294 alive / 35 gold
- HTTPS: 200 alive / 9 gold
- SOCKS4: 235 alive / 143 gold
- SOCKS5: 239 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14210
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
