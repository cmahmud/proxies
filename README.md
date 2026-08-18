# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 268
- HTTP: 384 alive / 24 gold
- HTTPS: 167 alive / 5 gold
- SOCKS4: 206 alive / 123 gold
- SOCKS5: 219 alive / 116 gold

## Historical pool

- Discovered: 102835
- Ever alive: 12955
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
