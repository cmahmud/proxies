# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 418
- HTTP: 342 alive / 89 gold
- HTTPS: 246 alive / 23 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 249 alive / 159 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29511
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
