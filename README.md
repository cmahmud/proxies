# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 409
- HTTP: 107 alive / 69 gold
- HTTPS: 89 alive / 19 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34956
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
