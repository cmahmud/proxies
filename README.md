# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 408
- HTTP: 98 alive / 54 gold
- HTTPS: 67 alive / 26 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45509
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
