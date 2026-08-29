# SyndProxy validated proxy pool

## Current pool

- Alive now: 354
- Gold now: 277
- HTTP: 39 alive / 24 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 154 alive / 123 gold
- SOCKS5: 156 alive / 129 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43622
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
