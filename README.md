# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 376
- HTTP: 333 alive / 85 gold
- HTTPS: 250 alive / 24 gold
- SOCKS4: 173 alive / 115 gold
- SOCKS5: 219 alive / 152 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29890
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
