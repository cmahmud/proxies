# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 366
- HTTP: 96 alive / 55 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33058
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
