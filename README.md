# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 407
- HTTP: 98 alive / 70 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43070
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
