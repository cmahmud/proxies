# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 416
- HTTP: 99 alive / 72 gold
- HTTPS: 80 alive / 16 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34855
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
