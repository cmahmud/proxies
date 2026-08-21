# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 379
- HTTP: 314 alive / 81 gold
- HTTPS: 237 alive / 22 gold
- SOCKS4: 222 alive / 138 gold
- SOCKS5: 220 alive / 138 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29366
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
