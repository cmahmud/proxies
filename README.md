# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 399
- HTTP: 183 alive / 79 gold
- HTTPS: 136 alive / 23 gold
- SOCKS4: 197 alive / 129 gold
- SOCKS5: 230 alive / 168 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27086
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
