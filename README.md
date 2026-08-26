# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 412
- HTTP: 106 alive / 68 gold
- HTTPS: 79 alive / 19 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38658
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
