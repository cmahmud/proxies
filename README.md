# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 451
- HTTP: 128 alive / 82 gold
- HTTPS: 91 alive / 37 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45605
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
