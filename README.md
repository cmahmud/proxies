# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 471
- HTTP: 138 alive / 94 gold
- HTTPS: 121 alive / 41 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44867
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
