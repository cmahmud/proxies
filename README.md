# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 378
- HTTP: 375 alive / 81 gold
- HTTPS: 261 alive / 26 gold
- SOCKS4: 181 alive / 117 gold
- SOCKS5: 235 alive / 154 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29894
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
