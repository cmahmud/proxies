# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 369
- HTTP: 362 alive / 71 gold
- HTTPS: 229 alive / 17 gold
- SOCKS4: 198 alive / 122 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15769
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
