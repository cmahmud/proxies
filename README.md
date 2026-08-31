# SyndProxy validated proxy pool

## Current pool

- Alive now: 718
- Gold now: 469
- HTTP: 174 alive / 92 gold
- HTTPS: 137 alive / 39 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 228 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45300
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
