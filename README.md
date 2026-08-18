# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 225
- HTTP: 200 alive / 22 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 188 alive / 118 gold
- SOCKS5: 195 alive / 77 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8069
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
