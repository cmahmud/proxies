# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 471
- HTTP: 166 alive / 102 gold
- HTTPS: 141 alive / 34 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45162
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
