# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 471
- HTTP: 154 alive / 98 gold
- HTTPS: 124 alive / 39 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45145
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
