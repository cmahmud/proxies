# SyndProxy validated proxy pool

## Current pool

- Alive now: 351
- Gold now: 308
- HTTP: 31 alive / 20 gold
- HTTPS: 4 alive / 0 gold
- SOCKS4: 156 alive / 148 gold
- SOCKS5: 160 alive / 140 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43615
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
