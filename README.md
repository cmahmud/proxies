# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 357
- HTTP: 87 alive / 49 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 152 alive / 148 gold
- SOCKS5: 157 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
