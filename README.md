# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 384
- HTTP: 108 alive / 54 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33478
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
