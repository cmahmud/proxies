# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 488
- HTTP: 341 alive / 141 gold
- HTTPS: 275 alive / 92 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 196 alive / 116 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
