# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 345
- HTTP: 333 alive / 51 gold
- HTTPS: 182 alive / 15 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 239 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14689
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
