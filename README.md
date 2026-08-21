# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 404
- HTTP: 214 alive / 88 gold
- HTTPS: 98 alive / 19 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 236 alive / 149 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29287
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
