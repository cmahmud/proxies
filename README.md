# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 430
- HTTP: 106 alive / 76 gold
- HTTPS: 52 alive / 27 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44457
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
