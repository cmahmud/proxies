# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 398
- HTTP: 319 alive / 91 gold
- HTTPS: 220 alive / 34 gold
- SOCKS4: 205 alive / 139 gold
- SOCKS5: 239 alive / 134 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31289
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
