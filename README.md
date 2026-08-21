# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 397
- HTTP: 292 alive / 88 gold
- HTTPS: 157 alive / 24 gold
- SOCKS4: 222 alive / 146 gold
- SOCKS5: 228 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29379
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
