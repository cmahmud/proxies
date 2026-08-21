# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 404
- HTTP: 223 alive / 89 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 220 alive / 148 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29287
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
