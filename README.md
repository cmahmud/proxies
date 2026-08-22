# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 432
- HTTP: 305 alive / 83 gold
- HTTPS: 227 alive / 27 gold
- SOCKS4: 238 alive / 156 gold
- SOCKS5: 264 alive / 166 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32012
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
