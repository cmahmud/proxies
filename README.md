# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 539
- HTTP: 431 alive / 162 gold
- HTTPS: 269 alive / 89 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 224 alive / 147 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18648
- Ever gold: 723

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
