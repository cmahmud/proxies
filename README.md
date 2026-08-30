# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 445
- HTTP: 144 alive / 91 gold
- HTTPS: 80 alive / 30 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44286
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
