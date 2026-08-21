# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 403
- HTTP: 315 alive / 83 gold
- HTTPS: 230 alive / 23 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 284 alive / 151 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29536
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
