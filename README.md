# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 460
- HTTP: 162 alive / 91 gold
- HTTPS: 134 alive / 34 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 223 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45312
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
