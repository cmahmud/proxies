# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 446
- HTTP: 116 alive / 80 gold
- HTTPS: 136 alive / 38 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44737
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
