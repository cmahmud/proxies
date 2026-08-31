# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 471
- HTTP: 159 alive / 101 gold
- HTTPS: 118 alive / 37 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45152
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
