# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 198
- HTTP: 431 alive / 23 gold
- HTTPS: 137 alive / 7 gold
- SOCKS4: 201 alive / 98 gold
- SOCKS5: 201 alive / 70 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8336
- Ever gold: 348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
