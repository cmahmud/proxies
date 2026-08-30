# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 427
- HTTP: 114 alive / 78 gold
- HTTPS: 60 alive / 21 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44534
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
