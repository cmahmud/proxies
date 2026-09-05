# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 273
- HTTP: 66 alive / 54 gold
- HTTPS: 60 alive / 22 gold
- SOCKS4: 132 alive / 64 gold
- SOCKS5: 264 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47761
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
