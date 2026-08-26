# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 398
- HTTP: 87 alive / 57 gold
- HTTPS: 66 alive / 15 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39066
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
