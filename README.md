# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 444
- HTTP: 115 alive / 81 gold
- HTTPS: 56 alive / 29 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43693
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
