# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 407
- HTTP: 271 alive / 83 gold
- HTTPS: 177 alive / 25 gold
- SOCKS4: 225 alive / 153 gold
- SOCKS5: 238 alive / 146 gold

## Historical pool

- Discovered: 156747
- Ever alive: 29596
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
