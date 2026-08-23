# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 375
- HTTP: 81 alive / 42 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 172323
- Ever alive: 32984
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
