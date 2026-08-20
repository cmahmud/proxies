# SyndProxy private pool

## Current pool

- Alive now: 1565
- Gold now: 651
- HTTP: 594 alive / 216 gold
- HTTPS: 486 alive / 110 gold
- SOCKS4: 235 alive / 157 gold
- SOCKS5: 250 alive / 168 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23944
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
