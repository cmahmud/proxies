# SyndProxy private pool

## Current pool

- Alive now: 1552
- Gold now: 653
- HTTP: 585 alive / 251 gold
- HTTPS: 452 alive / 117 gold
- SOCKS4: 209 alive / 126 gold
- SOCKS5: 306 alive / 159 gold

## Historical pool

- Discovered: 143487
- Ever alive: 24804
- Ever gold: 1046

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
