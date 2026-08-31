# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 441
- HTTP: 143 alive / 81 gold
- HTTPS: 104 alive / 29 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 212 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45426
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
