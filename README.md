# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 444
- HTTP: 118 alive / 79 gold
- HTTPS: 135 alive / 33 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44656
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
