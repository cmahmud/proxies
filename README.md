# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 285
- HTTP: 350 alive / 30 gold
- HTTPS: 179 alive / 6 gold
- SOCKS4: 252 alive / 125 gold
- SOCKS5: 244 alive / 124 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13131
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
