# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 347
- HTTP: 49 alive / 34 gold
- HTTPS: 10 alive / 1 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 166 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43601
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
