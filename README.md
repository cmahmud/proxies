# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 440
- HTTP: 114 alive / 75 gold
- HTTPS: 78 alive / 31 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45557
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
