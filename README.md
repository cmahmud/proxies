# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 352
- HTTP: 77 alive / 45 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 156 alive / 149 gold
- SOCKS5: 154 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
