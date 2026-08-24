# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 406
- HTTP: 113 alive / 63 gold
- HTTPS: 42 alive / 18 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33671
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
