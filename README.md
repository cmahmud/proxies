# SyndProxy private pool

## Current pool

- Alive now: 1538
- Gold now: 631
- HTTP: 517 alive / 210 gold
- HTTPS: 438 alive / 113 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 349 alive / 159 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24096
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
