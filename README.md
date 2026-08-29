# SyndProxy validated proxy pool

## Current pool

- Alive now: 357
- Gold now: 315
- HTTP: 34 alive / 22 gold
- HTTPS: 5 alive / 0 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 160 alive / 141 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43615
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
