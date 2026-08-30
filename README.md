# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 471
- HTTP: 138 alive / 98 gold
- HTTPS: 120 alive / 41 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44919
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
