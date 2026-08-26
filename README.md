# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 411
- HTTP: 101 alive / 65 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38637
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
