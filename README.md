# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 377
- HTTP: 279 alive / 78 gold
- HTTPS: 195 alive / 24 gold
- SOCKS4: 190 alive / 122 gold
- SOCKS5: 231 alive / 153 gold

## Historical pool

- Discovered: 164975
- Ever alive: 32259
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
