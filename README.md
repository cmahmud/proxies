# SyndProxy private pool

## Current pool

- Alive now: 1482
- Gold now: 587
- HTTP: 536 alive / 200 gold
- HTTPS: 417 alive / 98 gold
- SOCKS4: 228 alive / 140 gold
- SOCKS5: 301 alive / 149 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23382
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
