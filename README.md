# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 243
- HTTP: 358 alive / 32 gold
- HTTPS: 156 alive / 7 gold
- SOCKS4: 232 alive / 139 gold
- SOCKS5: 157 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13637
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
