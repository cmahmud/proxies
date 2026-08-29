# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 377
- HTTP: 74 alive / 51 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 173 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43493
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
