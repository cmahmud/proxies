# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 481
- HTTP: 145 alive / 99 gold
- HTTPS: 118 alive / 43 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45103
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
