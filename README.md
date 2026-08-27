# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 410
- HTTP: 84 alive / 62 gold
- HTTPS: 76 alive / 16 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41565
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
