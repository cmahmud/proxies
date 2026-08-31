# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 412
- HTTP: 92 alive / 60 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45517
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
