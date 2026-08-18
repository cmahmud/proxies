# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 369
- HTTP: 294 alive / 60 gold
- HTTPS: 205 alive / 14 gold
- SOCKS4: 233 alive / 151 gold
- SOCKS5: 220 alive / 144 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15187
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
