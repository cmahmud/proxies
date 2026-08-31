# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 442
- HTTP: 133 alive / 73 gold
- HTTPS: 114 alive / 33 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 219 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45377
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
