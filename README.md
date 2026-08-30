# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 439
- HTTP: 121 alive / 84 gold
- HTTPS: 69 alive / 33 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 201 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44150
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
