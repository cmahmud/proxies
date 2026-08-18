# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 324
- HTTP: 258 alive / 39 gold
- HTTPS: 179 alive / 9 gold
- SOCKS4: 211 alive / 140 gold
- SOCKS5: 227 alive / 136 gold

## Historical pool

- Discovered: 102931
- Ever alive: 13994
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
