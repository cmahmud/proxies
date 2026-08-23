# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 375
- HTTP: 91 alive / 47 gold
- HTTPS: 44 alive / 11 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 191 alive / 161 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32963
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
