# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 405
- HTTP: 113 alive / 64 gold
- HTTPS: 50 alive / 17 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33667
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
