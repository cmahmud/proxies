# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 421
- HTTP: 89 alive / 71 gold
- HTTPS: 100 alive / 21 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42555
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
