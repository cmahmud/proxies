# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 449
- HTTP: 134 alive / 82 gold
- HTTPS: 88 alive / 35 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45600
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
