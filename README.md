# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 433
- HTTP: 125 alive / 83 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43660
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
