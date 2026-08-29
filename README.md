# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 400
- HTTP: 91 alive / 67 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43265
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
