# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 418
- HTTP: 342 alive / 103 gold
- HTTPS: 253 alive / 35 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 224 alive / 141 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30697
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
