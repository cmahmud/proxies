# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 396
- HTTP: 91 alive / 65 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37271
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
