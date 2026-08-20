# SyndProxy private pool

## Current pool

- Alive now: 659
- Gold now: 354
- HTTP: 169 alive / 70 gold
- HTTPS: 112 alive / 22 gold
- SOCKS4: 182 alive / 124 gold
- SOCKS5: 196 alive / 138 gold

## Historical pool

- Discovered: 145580
- Ever alive: 25581
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
