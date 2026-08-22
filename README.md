# SyndProxy private pool

## Current pool

- Alive now: 758
- Gold now: 366
- HTTP: 218 alive / 86 gold
- HTTPS: 139 alive / 27 gold
- SOCKS4: 177 alive / 119 gold
- SOCKS5: 224 alive / 134 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
