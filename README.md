# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 442
- HTTP: 101 alive / 77 gold
- HTTPS: 84 alive / 35 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44611
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
