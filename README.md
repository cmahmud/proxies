# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 378
- HTTP: 194 alive / 76 gold
- HTTPS: 120 alive / 22 gold
- SOCKS4: 203 alive / 141 gold
- SOCKS5: 185 alive / 139 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25638
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
