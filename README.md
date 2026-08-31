# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 468
- HTTP: 164 alive / 97 gold
- HTTPS: 119 alive / 35 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 220 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45308
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
