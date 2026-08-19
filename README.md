# SyndProxy private pool

## Current pool

- Alive now: 1348
- Gold now: 399
- HTTP: 443 alive / 90 gold
- HTTPS: 296 alive / 17 gold
- SOCKS4: 240 alive / 127 gold
- SOCKS5: 369 alive / 165 gold

## Historical pool

- Discovered: 133936
- Ever alive: 21459
- Ever gold: 881

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
