# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 225
- HTTP: 234 alive / 32 gold
- HTTPS: 156 alive / 8 gold
- SOCKS4: 215 alive / 113 gold
- SOCKS5: 213 alive / 72 gold

## Historical pool

- Discovered: 93732
- Ever alive: 9326
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
