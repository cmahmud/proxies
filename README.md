# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 533
- HTTP: 397 alive / 158 gold
- HTTPS: 259 alive / 86 gold
- SOCKS4: 236 alive / 150 gold
- SOCKS5: 216 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18069
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
