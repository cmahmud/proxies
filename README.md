# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 335
- HTTP: 281 alive / 58 gold
- HTTPS: 210 alive / 12 gold
- SOCKS4: 229 alive / 139 gold
- SOCKS5: 221 alive / 126 gold

## Historical pool

- Discovered: 129285
- Ever alive: 20265
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
