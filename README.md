# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 381
- HTTP: 120 alive / 61 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 153 alive / 146 gold
- SOCKS5: 170 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38927
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
