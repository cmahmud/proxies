# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 471
- HTTP: 148 alive / 98 gold
- HTTPS: 126 alive / 38 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45145
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
