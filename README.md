# SyndProxy private pool

## Current pool

- Alive now: 1192
- Gold now: 403
- HTTP: 371 alive / 94 gold
- HTTPS: 257 alive / 17 gold
- SOCKS4: 232 alive / 146 gold
- SOCKS5: 332 alive / 146 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21200
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
