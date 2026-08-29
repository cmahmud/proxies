# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 382
- HTTP: 95 alive / 60 gold
- HTTPS: 52 alive / 21 gold
- SOCKS4: 155 alive / 151 gold
- SOCKS5: 163 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
