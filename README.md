# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 397
- HTTP: 219 alive / 91 gold
- HTTPS: 115 alive / 26 gold
- SOCKS4: 182 alive / 122 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 156421
- Ever alive: 29475
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
