# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 407
- HTTP: 83 alive / 63 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38533
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
