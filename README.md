# SyndProxy private pool

## Current pool

- Alive now: 1435
- Gold now: 595
- HTTP: 530 alive / 198 gold
- HTTPS: 405 alive / 94 gold
- SOCKS4: 246 alive / 146 gold
- SOCKS5: 254 alive / 157 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23578
- Ever gold: 923

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
