# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 444
- HTTP: 120 alive / 80 gold
- HTTPS: 122 alive / 35 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44729
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
