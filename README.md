# SyndProxy private pool

## Current pool

- Alive now: 549
- Gold now: 219
- HTTP: 154 alive / 37 gold
- HTTPS: 86 alive / 10 gold
- SOCKS4: 150 alive / 100 gold
- SOCKS5: 159 alive / 72 gold

## Historical pool

- Discovered: 82965
- Ever alive: 5062
- Ever gold: 286

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
