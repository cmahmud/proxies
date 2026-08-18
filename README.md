# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 342
- HTTP: 416 alive / 51 gold
- HTTPS: 184 alive / 9 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 219 alive / 139 gold

## Historical pool

- Discovered: 107060
- Ever alive: 14636
- Ever gold: 467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
