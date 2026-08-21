# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 409
- HTTP: 245 alive / 88 gold
- HTTPS: 172 alive / 24 gold
- SOCKS4: 208 alive / 140 gold
- SOCKS5: 251 alive / 157 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29069
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
