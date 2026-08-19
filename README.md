# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 407
- HTTP: 414 alive / 93 gold
- HTTPS: 246 alive / 17 gold
- SOCKS4: 233 alive / 143 gold
- SOCKS5: 263 alive / 154 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20884
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
