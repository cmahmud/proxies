# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 367
- HTTP: 298 alive / 61 gold
- HTTPS: 190 alive / 14 gold
- SOCKS4: 223 alive / 145 gold
- SOCKS5: 222 alive / 147 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15187
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
