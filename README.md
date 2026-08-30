# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 442
- HTTP: 120 alive / 79 gold
- HTTPS: 113 alive / 34 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44643
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
