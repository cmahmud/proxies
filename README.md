# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 450
- HTTP: 313 alive / 102 gold
- HTTPS: 231 alive / 30 gold
- SOCKS4: 201 alive / 152 gold
- SOCKS5: 258 alive / 166 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28744
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
