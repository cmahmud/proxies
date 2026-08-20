# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 402
- HTTP: 357 alive / 88 gold
- HTTPS: 252 alive / 26 gold
- SOCKS4: 194 alive / 134 gold
- SOCKS5: 222 alive / 154 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24927
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
