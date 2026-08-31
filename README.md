# SyndProxy validated proxy pool

## Current pool

- Alive now: 723
- Gold now: 471
- HTTP: 176 alive / 93 gold
- HTTPS: 126 alive / 39 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 247 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45283
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
