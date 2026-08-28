# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 395
- HTTP: 71 alive / 55 gold
- HTTPS: 32 alive / 16 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
