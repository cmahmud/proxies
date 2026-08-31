# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 471
- HTTP: 149 alive / 99 gold
- HTTPS: 117 alive / 35 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45128
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
