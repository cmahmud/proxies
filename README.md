# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 418
- HTTP: 92 alive / 70 gold
- HTTPS: 113 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42529
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
