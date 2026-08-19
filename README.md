# SyndProxy private pool

## Current pool

- Alive now: 1256
- Gold now: 545
- HTTP: 449 alive / 171 gold
- HTTPS: 369 alive / 78 gold
- SOCKS4: 232 alive / 148 gold
- SOCKS5: 206 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19757
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
