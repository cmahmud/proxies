# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 425
- HTTP: 138 alive / 75 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35186
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
