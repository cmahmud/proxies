# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 466
- HTTP: 123 alive / 93 gold
- HTTPS: 59 alive / 34 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49383
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
