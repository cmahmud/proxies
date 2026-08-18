# SyndProxy private pool

## Current pool

- Alive now: 573
- Gold now: 230
- HTTP: 139 alive / 28 gold
- HTTPS: 68 alive / 8 gold
- SOCKS4: 170 alive / 111 gold
- SOCKS5: 196 alive / 83 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8361
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
