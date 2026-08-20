# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 388
- HTTP: 219 alive / 78 gold
- HTTPS: 137 alive / 17 gold
- SOCKS4: 215 alive / 142 gold
- SOCKS5: 230 alive / 151 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25966
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
