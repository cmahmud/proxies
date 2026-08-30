# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 424
- HTTP: 112 alive / 72 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 201 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44466
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
