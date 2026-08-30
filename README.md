# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 430
- HTTP: 111 alive / 80 gold
- HTTPS: 59 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44313
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
