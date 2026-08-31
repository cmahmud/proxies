# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 446
- HTTP: 149 alive / 81 gold
- HTTPS: 103 alive / 31 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 215 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45449
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
