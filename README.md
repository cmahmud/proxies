# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 426
- HTTP: 95 alive / 71 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 179 alive / 167 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49053
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
