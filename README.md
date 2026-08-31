# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 424
- HTTP: 93 alive / 67 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45486
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
