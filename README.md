# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 389
- HTTP: 297 alive / 84 gold
- HTTPS: 193 alive / 21 gold
- SOCKS4: 207 alive / 145 gold
- SOCKS5: 213 alive / 139 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25313
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
