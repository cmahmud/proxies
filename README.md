# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 446
- HTTP: 130 alive / 80 gold
- HTTPS: 96 alive / 32 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 208 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45385
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
