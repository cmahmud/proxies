# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 402
- HTTP: 328 alive / 88 gold
- HTTPS: 220 alive / 27 gold
- SOCKS4: 200 alive / 132 gold
- SOCKS5: 235 alive / 155 gold

## Historical pool

- Discovered: 144731
- Ever alive: 24935
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
