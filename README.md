# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 345
- HTTP: 335 alive / 50 gold
- HTTPS: 191 alive / 11 gold
- SOCKS4: 234 alive / 145 gold
- SOCKS5: 223 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14650
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
