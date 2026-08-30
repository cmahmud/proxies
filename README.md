# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 427
- HTTP: 123 alive / 73 gold
- HTTPS: 69 alive / 27 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44374
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
