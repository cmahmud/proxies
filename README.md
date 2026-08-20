# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 361
- HTTP: 206 alive / 65 gold
- HTTPS: 124 alive / 15 gold
- SOCKS4: 175 alive / 141 gold
- SOCKS5: 204 alive / 140 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25655
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
