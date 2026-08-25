# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 410
- HTTP: 106 alive / 69 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34957
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
