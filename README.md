# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 412
- HTTP: 108 alive / 70 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33711
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
