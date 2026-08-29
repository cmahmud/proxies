# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 362
- HTTP: 55 alive / 38 gold
- HTTPS: 40 alive / 5 gold
- SOCKS4: 159 alive / 157 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43581
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
