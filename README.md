# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 389
- HTTP: 74 alive / 52 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36545
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
