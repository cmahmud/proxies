# SyndProxy private pool

## Current pool

- Alive now: 1456
- Gold now: 561
- HTTP: 565 alive / 181 gold
- HTTPS: 351 alive / 88 gold
- SOCKS4: 222 alive / 140 gold
- SOCKS5: 318 alive / 152 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22721
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
