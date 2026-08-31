# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 439
- HTTP: 136 alive / 76 gold
- HTTPS: 100 alive / 30 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 219 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45402
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
