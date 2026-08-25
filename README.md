# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 407
- HTTP: 107 alive / 65 gold
- HTTPS: 87 alive / 19 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35460
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
