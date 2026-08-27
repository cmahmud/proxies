# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 414
- HTTP: 115 alive / 64 gold
- HTTPS: 155 alive / 19 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41259
- Ever gold: 1320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
