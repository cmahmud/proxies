# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 399
- HTTP: 102 alive / 63 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 167 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37287
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
