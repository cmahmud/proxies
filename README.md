# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 406
- HTTP: 254 alive / 89 gold
- HTTPS: 137 alive / 20 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 224 alive / 157 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29454
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
