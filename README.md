# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 409
- HTTP: 110 alive / 67 gold
- HTTPS: 103 alive / 15 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38073
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
