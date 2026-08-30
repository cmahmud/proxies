# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 441
- HTTP: 133 alive / 88 gold
- HTTPS: 90 alive / 28 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44287
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
