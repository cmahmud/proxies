# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 394
- HTTP: 391 alive / 92 gold
- HTTPS: 269 alive / 13 gold
- SOCKS4: 245 alive / 139 gold
- SOCKS5: 284 alive / 150 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21061
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
