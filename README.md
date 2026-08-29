# SyndProxy validated proxy pool

## Current pool

- Alive now: 365
- Gold now: 317
- HTTP: 42 alive / 24 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 163 alive / 139 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43608
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
