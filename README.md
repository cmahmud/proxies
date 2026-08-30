# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 440
- HTTP: 115 alive / 77 gold
- HTTPS: 100 alive / 34 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44618
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
