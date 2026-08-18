# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 249
- HTTP: 325 alive / 30 gold
- HTTPS: 157 alive / 7 gold
- SOCKS4: 237 alive / 117 gold
- SOCKS5: 233 alive / 95 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9081
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
