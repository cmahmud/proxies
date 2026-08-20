# SyndProxy private pool

## Current pool

- Alive now: 692
- Gold now: 376
- HTTP: 202 alive / 74 gold
- HTTPS: 96 alive / 19 gold
- SOCKS4: 196 alive / 141 gold
- SOCKS5: 198 alive / 142 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25627
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
