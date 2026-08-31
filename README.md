# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 431
- HTTP: 124 alive / 72 gold
- HTTPS: 67 alive / 27 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45533
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
