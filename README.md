# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 451
- HTTP: 124 alive / 84 gold
- HTTPS: 83 alive / 34 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45577
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
