# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 417
- HTTP: 117 alive / 83 gold
- HTTPS: 66 alive / 27 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 172 alive / 157 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43697
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
