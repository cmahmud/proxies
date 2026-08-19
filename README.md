# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 497
- HTTP: 317 alive / 150 gold
- HTTPS: 232 alive / 89 gold
- SOCKS4: 211 alive / 122 gold
- SOCKS5: 219 alive / 136 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17578
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
