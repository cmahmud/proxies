# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 411
- HTTP: 329 alive / 87 gold
- HTTPS: 223 alive / 25 gold
- SOCKS4: 223 alive / 145 gold
- SOCKS5: 259 alive / 154 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29516
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
