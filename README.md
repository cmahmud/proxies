# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 385
- HTTP: 248 alive / 88 gold
- HTTPS: 170 alive / 28 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 208 alive / 130 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31601
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
