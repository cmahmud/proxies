# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 390
- HTTP: 256 alive / 83 gold
- HTTPS: 203 alive / 23 gold
- SOCKS4: 197 alive / 132 gold
- SOCKS5: 202 alive / 152 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27267
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
