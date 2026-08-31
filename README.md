# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 440
- HTTP: 150 alive / 79 gold
- HTTPS: 106 alive / 29 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 214 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45411
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
