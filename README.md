# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 408
- HTTP: 106 alive / 65 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38369
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
