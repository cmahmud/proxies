# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 347
- HTTP: 98 alive / 70 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 91 alive / 88 gold
- SOCKS5: 174 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48687
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
