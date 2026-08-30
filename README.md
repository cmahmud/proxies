# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 427
- HTTP: 115 alive / 74 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44358
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
