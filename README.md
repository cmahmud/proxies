# SyndProxy private pool

## Current pool

- Alive now: 1301
- Gold now: 419
- HTTP: 453 alive / 92 gold
- HTTPS: 297 alive / 17 gold
- SOCKS4: 257 alive / 153 gold
- SOCKS5: 294 alive / 157 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20865
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
