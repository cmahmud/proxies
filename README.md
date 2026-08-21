# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 400
- HTTP: 329 alive / 80 gold
- HTTPS: 216 alive / 21 gold
- SOCKS4: 234 alive / 147 gold
- SOCKS5: 273 alive / 152 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29546
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
