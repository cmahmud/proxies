# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 446
- HTTP: 126 alive / 87 gold
- HTTPS: 72 alive / 36 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 205 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44130
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
