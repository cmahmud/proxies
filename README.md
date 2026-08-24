# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 391
- HTTP: 123 alive / 69 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 179 alive / 151 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33279
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
