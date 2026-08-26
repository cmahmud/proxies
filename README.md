# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 408
- HTTP: 92 alive / 62 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39012
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
