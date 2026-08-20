# SyndProxy private pool

## Current pool

- Alive now: 1625
- Gold now: 632
- HTTP: 645 alive / 232 gold
- HTTPS: 509 alive / 120 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 260 alive / 144 gold

## Historical pool

- Discovered: 142739
- Ever alive: 24589
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
