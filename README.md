# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 526
- HTTP: 365 alive / 162 gold
- HTTPS: 259 alive / 90 gold
- SOCKS4: 205 alive / 124 gold
- SOCKS5: 218 alive / 150 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19188
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
