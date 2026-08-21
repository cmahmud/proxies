# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 409
- HTTP: 366 alive / 86 gold
- HTTPS: 236 alive / 24 gold
- SOCKS4: 231 alive / 147 gold
- SOCKS5: 282 alive / 152 gold

## Historical pool

- Discovered: 156429
- Ever alive: 29530
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
