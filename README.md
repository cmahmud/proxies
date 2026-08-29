# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 361
- HTTP: 53 alive / 43 gold
- HTTPS: 41 alive / 6 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 169 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43535
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
