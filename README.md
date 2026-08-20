# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 363
- HTTP: 213 alive / 75 gold
- HTTPS: 199 alive / 14 gold
- SOCKS4: 210 alive / 136 gold
- SOCKS5: 207 alive / 138 gold

## Historical pool

- Discovered: 149421
- Ever alive: 26539
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
