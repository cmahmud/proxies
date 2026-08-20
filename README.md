# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 394
- HTTP: 260 alive / 86 gold
- HTTPS: 209 alive / 23 gold
- SOCKS4: 197 alive / 132 gold
- SOCKS5: 210 alive / 153 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27264
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
