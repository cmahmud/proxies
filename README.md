# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 445
- HTTP: 120 alive / 90 gold
- HTTPS: 81 alive / 31 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44288
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
