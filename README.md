# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 405
- HTTP: 97 alive / 67 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43035
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
