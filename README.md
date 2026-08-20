# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 369
- HTTP: 169 alive / 69 gold
- HTTPS: 113 alive / 17 gold
- SOCKS4: 187 alive / 142 gold
- SOCKS5: 195 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25650
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
