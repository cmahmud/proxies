# SyndProxy validated proxy pool

## Current pool

- Alive now: 329
- Gold now: 266
- HTTP: 32 alive / 20 gold
- HTTPS: 5 alive / 0 gold
- SOCKS4: 147 alive / 129 gold
- SOCKS5: 145 alive / 117 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43629
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
