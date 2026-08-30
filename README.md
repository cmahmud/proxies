# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 439
- HTTP: 118 alive / 81 gold
- HTTPS: 74 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44299
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
