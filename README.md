# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 250
- HTTP: 326 alive / 35 gold
- HTTPS: 203 alive / 8 gold
- SOCKS4: 233 alive / 141 gold
- SOCKS5: 174 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13716
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
