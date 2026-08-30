# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 447
- HTTP: 115 alive / 81 gold
- HTTPS: 129 alive / 37 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44731
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
