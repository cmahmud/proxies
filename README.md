# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 399
- HTTP: 93 alive / 60 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38708
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
