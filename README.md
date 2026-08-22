# SyndProxy private pool

## Current pool

- Alive now: 1319
- Gold now: 408
- HTTP: 543 alive / 95 gold
- HTTPS: 328 alive / 32 gold
- SOCKS4: 219 alive / 139 gold
- SOCKS5: 229 alive / 142 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31728
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
