# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 443
- HTTP: 114 alive / 83 gold
- HTTPS: 63 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44579
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
