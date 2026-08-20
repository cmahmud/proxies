# SyndProxy private pool

## Current pool

- Alive now: 696
- Gold now: 376
- HTTP: 185 alive / 74 gold
- HTTPS: 116 alive / 22 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 189 alive / 139 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25640
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
