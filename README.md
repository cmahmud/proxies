# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 407
- HTTP: 101 alive / 62 gold
- HTTPS: 95 alive / 15 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39292
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
