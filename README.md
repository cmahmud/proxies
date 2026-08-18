# SyndProxy private pool

## Current pool

- Alive now: 610
- Gold now: 225
- HTTP: 194 alive / 36 gold
- HTTPS: 98 alive / 9 gold
- SOCKS4: 162 alive / 105 gold
- SOCKS5: 156 alive / 75 gold

## Historical pool

- Discovered: 86675
- Ever alive: 5731
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
