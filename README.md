# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 399
- HTTP: 218 alive / 84 gold
- HTTPS: 102 alive / 20 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 215 alive / 153 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25979
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
