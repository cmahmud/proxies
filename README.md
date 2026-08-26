# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 406
- HTTP: 90 alive / 62 gold
- HTTPS: 85 alive / 19 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38469
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
