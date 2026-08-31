# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 470
- HTTP: 155 alive / 101 gold
- HTTPS: 120 alive / 37 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45155
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
