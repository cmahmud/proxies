# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 462
- HTTP: 166 alive / 92 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 222 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45312
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
