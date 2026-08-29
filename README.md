# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 395
- HTTP: 86 alive / 69 gold
- HTTPS: 100 alive / 15 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43274
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
