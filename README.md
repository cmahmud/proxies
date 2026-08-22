# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 407
- HTTP: 285 alive / 91 gold
- HTTPS: 188 alive / 29 gold
- SOCKS4: 231 alive / 150 gold
- SOCKS5: 231 alive / 137 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31322
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
