# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 402
- HTTP: 80 alive / 56 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41595
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
