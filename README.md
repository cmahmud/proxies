# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 439
- HTTP: 120 alive / 80 gold
- HTTPS: 63 alive / 30 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 196 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44582
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
