# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 443
- HTTP: 120 alive / 75 gold
- HTTPS: 148 alive / 39 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44673
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
