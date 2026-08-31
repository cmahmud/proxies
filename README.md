# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 479
- HTTP: 148 alive / 99 gold
- HTTPS: 126 alive / 43 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45032
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
