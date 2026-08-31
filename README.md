# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 471
- HTTP: 136 alive / 95 gold
- HTTPS: 107 alive / 39 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45116
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
