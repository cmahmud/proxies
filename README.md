# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 402
- HTTP: 134 alive / 71 gold
- HTTPS: 39 alive / 15 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33278
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
