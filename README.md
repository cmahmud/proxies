# SyndProxy validated proxy pool

## Current pool

- Alive now: 332
- Gold now: 256
- HTTP: 35 alive / 21 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 148 alive / 123 gold
- SOCKS5: 146 alive / 112 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43629
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
