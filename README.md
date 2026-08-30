# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 421
- HTTP: 122 alive / 71 gold
- HTTPS: 70 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44396
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
