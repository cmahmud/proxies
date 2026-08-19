# SyndProxy private pool

## Current pool

- Alive now: 1368
- Gold now: 417
- HTTP: 491 alive / 86 gold
- HTTPS: 349 alive / 17 gold
- SOCKS4: 261 alive / 156 gold
- SOCKS5: 267 alive / 158 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20840
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
