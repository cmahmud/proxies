# SyndProxy private pool

## Current pool

- Alive now: 1506
- Gold now: 654
- HTTP: 582 alive / 251 gold
- HTTPS: 444 alive / 118 gold
- SOCKS4: 200 alive / 127 gold
- SOCKS5: 280 alive / 158 gold

## Historical pool

- Discovered: 143487
- Ever alive: 24796
- Ever gold: 1046

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
