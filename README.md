# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 399
- HTTP: 206 alive / 88 gold
- HTTPS: 158 alive / 31 gold
- SOCKS4: 201 alive / 127 gold
- SOCKS5: 244 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31925
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
