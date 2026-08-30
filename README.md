# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 443
- HTTP: 123 alive / 80 gold
- HTTPS: 123 alive / 34 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44729
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
