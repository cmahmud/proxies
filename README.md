# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 376
- HTTP: 289 alive / 84 gold
- HTTPS: 178 alive / 23 gold
- SOCKS4: 205 alive / 113 gold
- SOCKS5: 251 alive / 156 gold

## Historical pool

- Discovered: 166338
- Ever alive: 32401
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
