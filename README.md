# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 428
- HTTP: 101 alive / 78 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42510
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
