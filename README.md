# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 534
- HTTP: 369 alive / 165 gold
- HTTPS: 240 alive / 89 gold
- SOCKS4: 218 alive / 133 gold
- SOCKS5: 219 alive / 147 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18724
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
