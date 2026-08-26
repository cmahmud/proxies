# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 406
- HTTP: 106 alive / 63 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38666
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
