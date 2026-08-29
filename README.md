# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 381
- HTTP: 88 alive / 59 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 155 alive / 152 gold
- SOCKS5: 164 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43647
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
