# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 411
- HTTP: 106 alive / 65 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38422
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
