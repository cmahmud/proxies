# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 394
- HTTP: 105 alive / 61 gold
- HTTPS: 75 alive / 11 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38275
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
