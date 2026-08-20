# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 391
- HTTP: 190 alive / 66 gold
- HTTPS: 95 alive / 21 gold
- SOCKS4: 194 alive / 150 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25754
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
