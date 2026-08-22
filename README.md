# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 438
- HTTP: 295 alive / 94 gold
- HTTPS: 219 alive / 32 gold
- SOCKS4: 192 alive / 140 gold
- SOCKS5: 247 alive / 172 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31254
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
