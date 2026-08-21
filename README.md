# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 432
- HTTP: 373 alive / 109 gold
- HTTPS: 245 alive / 27 gold
- SOCKS4: 234 alive / 154 gold
- SOCKS5: 244 alive / 142 gold

## Historical pool

- Discovered: 160024
- Ever alive: 30557
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
