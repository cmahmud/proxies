# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 469
- HTTP: 135 alive / 100 gold
- HTTPS: 56 alive / 34 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49360
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
