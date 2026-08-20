# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 379
- HTTP: 239 alive / 77 gold
- HTTPS: 166 alive / 23 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 248 alive / 140 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25286
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
