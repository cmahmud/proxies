# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 405
- HTTP: 181 alive / 87 gold
- HTTPS: 130 alive / 22 gold
- SOCKS4: 183 alive / 129 gold
- SOCKS5: 223 alive / 167 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27096
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
