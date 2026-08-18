# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 195
- HTTP: 349 alive / 23 gold
- HTTPS: 143 alive / 7 gold
- SOCKS4: 201 alive / 96 gold
- SOCKS5: 203 alive / 69 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8336
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
