# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 474
- HTTP: 160 alive / 104 gold
- HTTPS: 140 alive / 36 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45160
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
