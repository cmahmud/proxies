# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 422
- HTTP: 293 alive / 104 gold
- HTTPS: 170 alive / 35 gold
- SOCKS4: 215 alive / 138 gold
- SOCKS5: 230 alive / 145 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30702
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
