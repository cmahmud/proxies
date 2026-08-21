# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 417
- HTTP: 327 alive / 91 gold
- HTTPS: 198 alive / 23 gold
- SOCKS4: 219 alive / 155 gold
- SOCKS5: 239 alive / 148 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30070
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
