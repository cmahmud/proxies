# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 437
- HTTP: 365 alive / 103 gold
- HTTPS: 232 alive / 28 gold
- SOCKS4: 220 alive / 139 gold
- SOCKS5: 268 alive / 167 gold

## Historical pool

- Discovered: 153117
- Ever alive: 28425
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
