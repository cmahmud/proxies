# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 292
- HTTP: 302 alive / 26 gold
- HTTPS: 185 alive / 4 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 216 alive / 120 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13514
- Ever gold: 417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
