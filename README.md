# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 388
- HTTP: 203 alive / 75 gold
- HTTPS: 124 alive / 19 gold
- SOCKS4: 202 alive / 140 gold
- SOCKS5: 213 alive / 154 gold

## Historical pool

- Discovered: 147183
- Ever alive: 25814
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
