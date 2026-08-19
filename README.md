# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 465
- HTTP: 412 alive / 124 gold
- HTTPS: 260 alive / 74 gold
- SOCKS4: 204 alive / 139 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16663
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
