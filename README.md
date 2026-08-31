# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 471
- HTTP: 133 alive / 96 gold
- HTTPS: 103 alive / 39 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45117
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
