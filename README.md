# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 420
- HTTP: 92 alive / 59 gold
- HTTPS: 68 alive / 29 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45498
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
