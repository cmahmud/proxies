# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 374
- HTTP: 309 alive / 82 gold
- HTTPS: 187 alive / 23 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 221 alive / 131 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32363
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
