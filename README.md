# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 382
- HTTP: 301 alive / 85 gold
- HTTPS: 200 alive / 23 gold
- SOCKS4: 167 alive / 107 gold
- SOCKS5: 240 alive / 167 gold

## Historical pool

- Discovered: 166622
- Ever alive: 32455
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
