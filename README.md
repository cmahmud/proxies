# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 382
- HTTP: 199 alive / 77 gold
- HTTPS: 125 alive / 20 gold
- SOCKS4: 224 alive / 146 gold
- SOCKS5: 198 alive / 139 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25491
- Ever gold: 1062

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
