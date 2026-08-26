# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 406
- HTTP: 112 alive / 63 gold
- HTTPS: 66 alive / 20 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38729
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
