# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 408
- HTTP: 87 alive / 62 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39010
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
