# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 227
- HTTP: 294 alive / 31 gold
- HTTPS: 165 alive / 8 gold
- SOCKS4: 229 alive / 124 gold
- SOCKS5: 152 alive / 64 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13518
- Ever gold: 424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
