# SyndProxy validated proxy pool

## Current pool

- Alive now: 378
- Gold now: 322
- HTTP: 56 alive / 33 gold
- HTTPS: 19 alive / 1 gold
- SOCKS4: 147 alive / 144 gold
- SOCKS5: 156 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43633
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
