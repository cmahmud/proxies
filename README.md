# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 449
- HTTP: 122 alive / 90 gold
- HTTPS: 66 alive / 36 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 203 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44261
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
