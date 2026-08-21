# SyndProxy private pool

## Current pool

- Alive now: 1433
- Gold now: 427
- HTTP: 561 alive / 101 gold
- HTTPS: 395 alive / 29 gold
- SOCKS4: 229 alive / 139 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30409
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
