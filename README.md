# SyndProxy private pool

## Current pool

- Alive now: 1221
- Gold now: 418
- HTTP: 448 alive / 97 gold
- HTTPS: 298 alive / 25 gold
- SOCKS4: 231 alive / 139 gold
- SOCKS5: 244 alive / 157 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30421
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
