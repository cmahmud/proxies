# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 402
- HTTP: 188 alive / 85 gold
- HTTPS: 125 alive / 22 gold
- SOCKS4: 188 alive / 129 gold
- SOCKS5: 225 alive / 166 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27100
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
