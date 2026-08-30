# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 447
- HTTP: 113 alive / 81 gold
- HTTPS: 71 alive / 35 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 203 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44585
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
