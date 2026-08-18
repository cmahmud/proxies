# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 324
- HTTP: 373 alive / 45 gold
- HTTPS: 213 alive / 11 gold
- SOCKS4: 242 alive / 137 gold
- SOCKS5: 236 alive / 131 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14409
- Ever gold: 448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
