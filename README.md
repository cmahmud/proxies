# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 383
- HTTP: 85 alive / 63 gold
- HTTPS: 87 alive / 15 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43279
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
