# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 422
- HTTP: 130 alive / 71 gold
- HTTPS: 88 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35076
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
