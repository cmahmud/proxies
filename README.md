# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 405
- HTTP: 81 alive / 60 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42747
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
