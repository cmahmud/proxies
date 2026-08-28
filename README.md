# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 406
- HTTP: 91 alive / 70 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43070
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
