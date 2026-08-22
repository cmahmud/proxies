# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 433
- HTTP: 314 alive / 93 gold
- HTTPS: 228 alive / 30 gold
- SOCKS4: 196 alive / 141 gold
- SOCKS5: 249 alive / 169 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31253
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
