# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 428
- HTTP: 96 alive / 70 gold
- HTTPS: 62 alive / 26 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45484
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
