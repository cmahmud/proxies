# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 423
- HTTP: 115 alive / 74 gold
- HTTPS: 97 alive / 24 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34930
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
