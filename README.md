# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 487
- HTTP: 330 alive / 140 gold
- HTTPS: 269 alive / 92 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 201 alive / 116 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17340
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
