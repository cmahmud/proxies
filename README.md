# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 391
- HTTP: 317 alive / 85 gold
- HTTPS: 158 alive / 26 gold
- SOCKS4: 207 alive / 145 gold
- SOCKS5: 243 alive / 135 gold

## Historical pool

- Discovered: 167116
- Ever alive: 32527
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
