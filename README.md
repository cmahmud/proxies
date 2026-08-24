# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 404
- HTTP: 114 alive / 64 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33671
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
