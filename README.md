# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 472
- HTTP: 174 alive / 98 gold
- HTTPS: 110 alive / 36 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 224 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45290
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
