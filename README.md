# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 471
- HTTP: 147 alive / 98 gold
- HTTPS: 106 alive / 38 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45139
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
