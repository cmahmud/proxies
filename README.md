# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 388
- HTTP: 200 alive / 77 gold
- HTTPS: 132 alive / 19 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 224 alive / 151 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25961
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
