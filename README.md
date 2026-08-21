# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 374
- HTTP: 345 alive / 83 gold
- HTTPS: 269 alive / 24 gold
- SOCKS4: 174 alive / 115 gold
- SOCKS5: 221 alive / 152 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29890
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
