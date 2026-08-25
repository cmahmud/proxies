# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 414
- HTTP: 125 alive / 69 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35238
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
