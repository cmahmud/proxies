# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 388
- HTTP: 209 alive / 89 gold
- HTTPS: 105 alive / 22 gold
- SOCKS4: 189 alive / 121 gold
- SOCKS5: 228 alive / 156 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29462
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
