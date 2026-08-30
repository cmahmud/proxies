# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 445
- HTTP: 117 alive / 81 gold
- HTTPS: 131 alive / 32 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44702
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
