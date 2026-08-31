# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 441
- HTTP: 155 alive / 79 gold
- HTTPS: 108 alive / 28 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 216 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45411
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
