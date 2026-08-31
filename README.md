# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 451
- HTTP: 137 alive / 81 gold
- HTTPS: 106 alive / 34 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 214 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45418
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
