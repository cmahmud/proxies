# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 455
- HTTP: 121 alive / 85 gold
- HTTPS: 114 alive / 39 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44773
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
