# SyndProxy private pool

## Current pool

- Alive now: 1469
- Gold now: 389
- HTTP: 530 alive / 101 gold
- HTTPS: 377 alive / 20 gold
- SOCKS4: 246 alive / 125 gold
- SOCKS5: 316 alive / 143 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22499
- Ever gold: 907

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
