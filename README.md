# SyndProxy private pool

## Current pool

- Alive now: 1657
- Gold now: 612
- HTTP: 613 alive / 217 gold
- HTTPS: 467 alive / 113 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 363 alive / 147 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23908
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
