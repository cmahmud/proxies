# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 411
- HTTP: 294 alive / 94 gold
- HTTPS: 216 alive / 31 gold
- SOCKS4: 241 alive / 149 gold
- SOCKS5: 232 alive / 137 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31319
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
