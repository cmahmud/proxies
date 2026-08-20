# SyndProxy private pool

## Current pool

- Alive now: 1441
- Gold now: 645
- HTTP: 532 alive / 234 gold
- HTTPS: 427 alive / 128 gold
- SOCKS4: 223 alive / 145 gold
- SOCKS5: 259 alive / 138 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24624
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
