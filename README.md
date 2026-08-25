# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 417
- HTTP: 96 alive / 70 gold
- HTTPS: 65 alive / 20 gold
- SOCKS4: 212 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37125
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
