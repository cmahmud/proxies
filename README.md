# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 537
- HTTP: 399 alive / 162 gold
- HTTPS: 281 alive / 93 gold
- SOCKS4: 208 alive / 141 gold
- SOCKS5: 225 alive / 141 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18596
- Ever gold: 721

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
