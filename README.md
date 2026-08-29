# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 377
- HTTP: 68 alive / 49 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 169 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43519
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
