# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 342
- HTTP: 99 alive / 37 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 174 alive / 152 gold
- SOCKS5: 169 alive / 143 gold

## Historical pool

- Discovered: 171059
- Ever alive: 32856
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
