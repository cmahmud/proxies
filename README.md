# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 442
- HTTP: 124 alive / 83 gold
- HTTPS: 92 alive / 34 gold
- SOCKS4: 187 alive / 159 gold
- SOCKS5: 202 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45580
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
