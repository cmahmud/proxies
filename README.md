# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 409
- HTTP: 99 alive / 63 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38475
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
