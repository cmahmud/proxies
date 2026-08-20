# SyndProxy private pool

## Current pool

- Alive now: 692
- Gold now: 381
- HTTP: 161 alive / 73 gold
- HTTPS: 121 alive / 21 gold
- SOCKS4: 197 alive / 139 gold
- SOCKS5: 213 alive / 148 gold

## Historical pool

- Discovered: 145562
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
