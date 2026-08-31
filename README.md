# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 410
- HTTP: 92 alive / 58 gold
- HTTPS: 67 alive / 21 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45504
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
