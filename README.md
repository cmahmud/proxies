# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 422
- HTTP: 113 alive / 72 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 200 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44466
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
