# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 430
- HTTP: 107 alive / 79 gold
- HTTPS: 46 alive / 23 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44520
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
