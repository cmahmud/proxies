# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 423
- HTTP: 131 alive / 72 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35078
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
