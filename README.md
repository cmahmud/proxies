# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 402
- HTTP: 81 alive / 55 gold
- HTTPS: 62 alive / 19 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41601
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
