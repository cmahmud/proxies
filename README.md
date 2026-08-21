# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 418
- HTTP: 211 alive / 93 gold
- HTTPS: 152 alive / 25 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 209 alive / 161 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27720
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
