# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 421
- HTTP: 97 alive / 71 gold
- HTTPS: 118 alive / 21 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42564
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
