# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 337
- HTTP: 319 alive / 66 gold
- HTTPS: 196 alive / 14 gold
- SOCKS4: 248 alive / 139 gold
- SOCKS5: 201 alive / 118 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15355
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
