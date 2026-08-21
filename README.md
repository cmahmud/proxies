# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 368
- HTTP: 298 alive / 94 gold
- HTTPS: 187 alive / 24 gold
- SOCKS4: 190 alive / 138 gold
- SOCKS5: 229 alive / 112 gold

## Historical pool

- Discovered: 154713
- Ever alive: 29001
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
