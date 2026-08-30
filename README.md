# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 447
- HTTP: 112 alive / 83 gold
- HTTPS: 49 alive / 30 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43681
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
