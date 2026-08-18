# SyndProxy private pool

## Current pool

- Alive now: 943
- Gold now: 346
- HTTP: 295 alive / 53 gold
- HTTPS: 184 alive / 14 gold
- SOCKS4: 229 alive / 139 gold
- SOCKS5: 235 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14692
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
