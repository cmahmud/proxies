# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 445
- HTTP: 119 alive / 78 gold
- HTTPS: 138 alive / 36 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44663
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
