# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 422
- HTTP: 319 alive / 84 gold
- HTTPS: 249 alive / 28 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 263 alive / 164 gold

## Historical pool

- Discovered: 158920
- Ever alive: 30141
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
