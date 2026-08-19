# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 359
- HTTP: 344 alive / 67 gold
- HTTPS: 218 alive / 17 gold
- SOCKS4: 227 alive / 154 gold
- SOCKS5: 233 alive / 121 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16105
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
