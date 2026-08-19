# SyndProxy private pool

## Current pool

- Alive now: 1311
- Gold now: 411
- HTTP: 436 alive / 82 gold
- HTTPS: 306 alive / 16 gold
- SOCKS4: 248 alive / 157 gold
- SOCKS5: 321 alive / 156 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21967
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
