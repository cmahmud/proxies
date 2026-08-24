# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 405
- HTTP: 113 alive / 64 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33671
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
