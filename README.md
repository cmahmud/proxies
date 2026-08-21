# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 399
- HTTP: 269 alive / 80 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 235 alive / 150 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29588
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
