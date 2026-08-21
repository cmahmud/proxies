# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 406
- HTTP: 231 alive / 93 gold
- HTTPS: 132 alive / 22 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 213 alive / 152 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27758
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
