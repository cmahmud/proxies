# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 422
- HTTP: 117 alive / 69 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35100
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
