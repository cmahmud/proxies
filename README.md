# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 441
- HTTP: 302 alive / 99 gold
- HTTPS: 203 alive / 35 gold
- SOCKS4: 201 alive / 147 gold
- SOCKS5: 267 alive / 160 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28691
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
