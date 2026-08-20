# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 375
- HTTP: 166 alive / 72 gold
- HTTPS: 130 alive / 17 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 207 alive / 141 gold

## Historical pool

- Discovered: 148339
- Ever alive: 26320
- Ever gold: 1081

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
