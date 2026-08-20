# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 363
- HTTP: 168 alive / 70 gold
- HTTPS: 103 alive / 23 gold
- SOCKS4: 184 alive / 130 gold
- SOCKS5: 197 alive / 140 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25577
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
