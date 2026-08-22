# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 370
- HTTP: 268 alive / 79 gold
- HTTPS: 153 alive / 23 gold
- SOCKS4: 179 alive / 118 gold
- SOCKS5: 218 alive / 150 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
