# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 454
- HTTP: 140 alive / 84 gold
- HTTPS: 105 alive / 35 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 208 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45420
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
