# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 396
- HTTP: 97 alive / 64 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 169 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37422
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
