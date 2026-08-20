# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 402
- HTTP: 192 alive / 85 gold
- HTTPS: 133 alive / 23 gold
- SOCKS4: 188 alive / 127 gold
- SOCKS5: 223 alive / 167 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27105
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
