# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 407
- HTTP: 110 alive / 64 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35454
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
