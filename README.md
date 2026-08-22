# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 425
- HTTP: 320 alive / 86 gold
- HTTPS: 250 alive / 29 gold
- SOCKS4: 210 alive / 144 gold
- SOCKS5: 256 alive / 166 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31238
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
