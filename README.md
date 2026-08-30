# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 436
- HTTP: 121 alive / 92 gold
- HTTPS: 70 alive / 31 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44094
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
