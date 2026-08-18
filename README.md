# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 203
- HTTP: 177 alive / 19 gold
- HTTPS: 104 alive / 8 gold
- SOCKS4: 170 alive / 99 gold
- SOCKS5: 196 alive / 77 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8044
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
