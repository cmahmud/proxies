# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 405
- HTTP: 315 alive / 80 gold
- HTTPS: 186 alive / 19 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 234 alive / 156 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32297
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
