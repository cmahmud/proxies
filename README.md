# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 407
- HTTP: 105 alive / 65 gold
- HTTPS: 105 alive / 15 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42578
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
