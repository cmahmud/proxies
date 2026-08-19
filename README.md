# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 386
- HTTP: 407 alive / 89 gold
- HTTPS: 283 alive / 16 gold
- SOCKS4: 215 alive / 129 gold
- SOCKS5: 311 alive / 152 gold

## Historical pool

- Discovered: 134541
- Ever alive: 21999
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
