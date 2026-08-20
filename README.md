# SyndProxy private pool

## Current pool

- Alive now: 1594
- Gold now: 632
- HTTP: 546 alive / 210 gold
- HTTPS: 451 alive / 113 gold
- SOCKS4: 243 alive / 150 gold
- SOCKS5: 354 alive / 159 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24095
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
