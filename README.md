# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 439
- HTTP: 119 alive / 80 gold
- HTTPS: 62 alive / 30 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44582
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
