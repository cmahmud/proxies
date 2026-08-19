# SyndProxy private pool

## Current pool

- Alive now: 1389
- Gold now: 396
- HTTP: 483 alive / 92 gold
- HTTPS: 345 alive / 20 gold
- SOCKS4: 236 alive / 128 gold
- SOCKS5: 325 alive / 156 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22025
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
