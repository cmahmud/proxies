# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 442
- HTTP: 121 alive / 81 gold
- HTTPS: 130 alive / 33 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44718
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
