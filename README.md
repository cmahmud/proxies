# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 396
- HTTP: 83 alive / 51 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41695
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
