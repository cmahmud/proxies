# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 430
- HTTP: 304 alive / 89 gold
- HTTPS: 232 alive / 25 gold
- SOCKS4: 244 alive / 156 gold
- SOCKS5: 269 alive / 160 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32204
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
