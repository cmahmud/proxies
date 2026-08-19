# SyndProxy private pool

## Current pool

- Alive now: 1426
- Gold now: 391
- HTTP: 488 alive / 90 gold
- HTTPS: 345 alive / 19 gold
- SOCKS4: 267 alive / 128 gold
- SOCKS5: 326 alive / 154 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22029
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
