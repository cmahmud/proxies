# SyndProxy private pool

## Current pool

- Alive now: 621
- Gold now: 204
- HTTP: 149 alive / 19 gold
- HTTPS: 94 alive / 8 gold
- SOCKS4: 173 alive / 100 gold
- SOCKS5: 205 alive / 77 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8007
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
