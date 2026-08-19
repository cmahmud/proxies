# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 553
- HTTP: 463 alive / 189 gold
- HTTPS: 276 alive / 105 gold
- SOCKS4: 238 alive / 119 gold
- SOCKS5: 220 alive / 140 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19286
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
