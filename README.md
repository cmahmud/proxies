# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 438
- HTTP: 120 alive / 81 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43689
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
