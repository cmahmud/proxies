# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 424
- HTTP: 91 alive / 66 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45477
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
