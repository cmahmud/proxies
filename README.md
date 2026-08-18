# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 199
- HTTP: 429 alive / 22 gold
- HTTPS: 143 alive / 8 gold
- SOCKS4: 213 alive / 99 gold
- SOCKS5: 202 alive / 70 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8336
- Ever gold: 348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
