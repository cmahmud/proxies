# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 427
- HTTP: 346 alive / 108 gold
- HTTPS: 203 alive / 32 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 244 alive / 148 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30713
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
