# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 249
- HTTP: 326 alive / 35 gold
- HTTPS: 200 alive / 8 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 165 alive / 64 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13705
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
