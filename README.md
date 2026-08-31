# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 454
- HTTP: 123 alive / 87 gold
- HTTPS: 91 alive / 36 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 198 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45604
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
