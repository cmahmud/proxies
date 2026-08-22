# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 438
- HTTP: 273 alive / 88 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 234 alive / 153 gold
- SOCKS5: 281 alive / 172 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32204
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
