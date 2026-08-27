# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 421
- HTTP: 101 alive / 69 gold
- HTTPS: 142 alive / 19 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41226
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
