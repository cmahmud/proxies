# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 591
- HTTP: 459 alive / 186 gold
- HTTPS: 301 alive / 129 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 210 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
