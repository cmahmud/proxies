# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 405
- HTTP: 95 alive / 61 gold
- HTTPS: 109 alive / 18 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41442
- Ever gold: 1331

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
