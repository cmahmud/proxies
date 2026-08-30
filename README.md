# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 448
- HTTP: 127 alive / 83 gold
- HTTPS: 149 alive / 33 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44706
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
