# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 405
- HTTP: 103 alive / 59 gold
- HTTPS: 103 alive / 19 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43025
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
