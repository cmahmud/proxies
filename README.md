# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 398
- HTTP: 203 alive / 90 gold
- HTTPS: 151 alive / 32 gold
- SOCKS4: 192 alive / 125 gold
- SOCKS5: 248 alive / 151 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31922
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
