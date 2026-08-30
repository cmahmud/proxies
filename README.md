# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 436
- HTTP: 111 alive / 84 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
