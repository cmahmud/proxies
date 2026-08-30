# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 416
- HTTP: 120 alive / 77 gold
- HTTPS: 83 alive / 28 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44042
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
