# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 410
- HTTP: 102 alive / 66 gold
- HTTPS: 89 alive / 19 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35433
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
