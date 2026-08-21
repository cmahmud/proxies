# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 383
- HTTP: 332 alive / 84 gold
- HTTPS: 226 alive / 25 gold
- SOCKS4: 217 alive / 135 gold
- SOCKS5: 228 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29371
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
