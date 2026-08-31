# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 446
- HTTP: 143 alive / 80 gold
- HTTPS: 98 alive / 31 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 215 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45430
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
