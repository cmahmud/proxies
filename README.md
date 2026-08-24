# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 396
- HTTP: 114 alive / 59 gold
- HTTPS: 40 alive / 13 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33663
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
