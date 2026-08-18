# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 194
- HTTP: 348 alive / 23 gold
- HTTPS: 123 alive / 7 gold
- SOCKS4: 197 alive / 96 gold
- SOCKS5: 204 alive / 68 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8312
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
