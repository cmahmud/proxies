# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 389
- HTTP: 102 alive / 63 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 154 alive / 146 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38761
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
