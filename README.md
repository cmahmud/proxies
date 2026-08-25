# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 414
- HTTP: 119 alive / 69 gold
- HTTPS: 99 alive / 20 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34952
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
