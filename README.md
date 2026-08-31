# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 472
- HTTP: 155 alive / 96 gold
- HTTPS: 118 alive / 36 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45248
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
