# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 469
- HTTP: 153 alive / 97 gold
- HTTPS: 107 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45135
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
