# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 438
- HTTP: 127 alive / 83 gold
- HTTPS: 76 alive / 29 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44300
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
