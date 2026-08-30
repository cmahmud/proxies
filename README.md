# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 446
- HTTP: 127 alive / 92 gold
- HTTPS: 69 alive / 33 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 202 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44241
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
