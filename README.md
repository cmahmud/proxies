# SyndProxy private pool

## Current pool

- Alive now: 654
- Gold now: 353
- HTTP: 163 alive / 68 gold
- HTTPS: 114 alive / 23 gold
- SOCKS4: 188 alive / 124 gold
- SOCKS5: 189 alive / 138 gold

## Historical pool

- Discovered: 145581
- Ever alive: 25583
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
