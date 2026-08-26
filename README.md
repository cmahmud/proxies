# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 381
- HTTP: 134 alive / 70 gold
- HTTPS: 176 alive / 16 gold
- SOCKS4: 161 alive / 145 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39809
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
