# SyndProxy private pool

## Current pool

- Alive now: 1571
- Gold now: 586
- HTTP: 651 alive / 198 gold
- HTTPS: 426 alive / 97 gold
- SOCKS4: 233 alive / 141 gold
- SOCKS5: 261 alive / 150 gold

## Historical pool

- Discovered: 136252
- Ever alive: 22768
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
