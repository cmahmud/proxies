# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 429
- HTTP: 142 alive / 87 gold
- HTTPS: 96 alive / 29 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 209 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43999
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
