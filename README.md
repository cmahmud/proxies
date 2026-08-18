# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 280
- HTTP: 287 alive / 24 gold
- HTTPS: 158 alive / 5 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 225 alive / 112 gold

## Historical pool

- Discovered: 102825
- Ever alive: 12816
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
