# SyndProxy validated proxy pool

## Current pool

- Alive now: 351
- Gold now: 297
- HTTP: 33 alive / 21 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 157 alive / 139 gold
- SOCKS5: 159 alive / 137 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43615
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
