# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 438
- HTTP: 109 alive / 82 gold
- HTTPS: 61 alive / 29 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44576
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
