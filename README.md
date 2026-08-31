# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 432
- HTTP: 112 alive / 72 gold
- HTTPS: 71 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45544
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
