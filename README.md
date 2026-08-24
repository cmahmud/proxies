# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 403
- HTTP: 114 alive / 63 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33671
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
