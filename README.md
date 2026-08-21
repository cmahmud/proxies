# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 412
- HTTP: 266 alive / 89 gold
- HTTPS: 159 alive / 26 gold
- SOCKS4: 197 alive / 141 gold
- SOCKS5: 241 alive / 156 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29449
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
