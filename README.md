# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 396
- HTTP: 271 alive / 87 gold
- HTTPS: 198 alive / 26 gold
- SOCKS4: 197 alive / 135 gold
- SOCKS5: 209 alive / 148 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27282
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
