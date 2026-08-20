# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 391
- HTTP: 213 alive / 81 gold
- HTTPS: 143 alive / 17 gold
- SOCKS4: 213 alive / 143 gold
- SOCKS5: 225 alive / 150 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25966
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
