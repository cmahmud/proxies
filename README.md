# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 423
- HTTP: 124 alive / 75 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35210
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
