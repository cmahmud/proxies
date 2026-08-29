# SyndProxy validated proxy pool

## Current pool

- Alive now: 359
- Gold now: 313
- HTTP: 52 alive / 28 gold
- HTTPS: 13 alive / 0 gold
- SOCKS4: 147 alive / 144 gold
- SOCKS5: 147 alive / 141 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43631
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
