# SyndProxy private pool

## Current pool

- Alive now: 608
- Gold now: 220
- HTTP: 195 alive / 35 gold
- HTTPS: 96 alive / 9 gold
- SOCKS4: 162 alive / 103 gold
- SOCKS5: 155 alive / 73 gold

## Historical pool

- Discovered: 86675
- Ever alive: 5733
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
