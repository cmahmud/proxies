# SyndProxy validated proxy pool

## Current pool

- Alive now: 355
- Gold now: 311
- HTTP: 33 alive / 18 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 157 alive / 149 gold
- SOCKS5: 162 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43615
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
