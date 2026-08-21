# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 407
- HTTP: 303 alive / 88 gold
- HTTPS: 197 alive / 32 gold
- SOCKS4: 200 alive / 131 gold
- SOCKS5: 262 alive / 156 gold

## Historical pool

- Discovered: 153847
- Ever alive: 28877
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
