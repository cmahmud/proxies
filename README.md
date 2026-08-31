# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 449
- HTTP: 149 alive / 81 gold
- HTTPS: 94 alive / 34 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 219 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45439
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
