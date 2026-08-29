# SyndProxy validated proxy pool

## Current pool

- Alive now: 351
- Gold now: 326
- HTTP: 33 alive / 21 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 156 alive / 155 gold
- SOCKS5: 159 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43615
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
