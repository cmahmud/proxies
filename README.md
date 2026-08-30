# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 442
- HTTP: 112 alive / 83 gold
- HTTPS: 63 alive / 31 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44579
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
