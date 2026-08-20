# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 407
- HTTP: 173 alive / 86 gold
- HTTPS: 127 alive / 23 gold
- SOCKS4: 189 alive / 129 gold
- SOCKS5: 224 alive / 169 gold

## Historical pool

- Discovered: 150985
- Ever alive: 27091
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
