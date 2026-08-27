# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 401
- HTTP: 74 alive / 53 gold
- HTTPS: 53 alive / 21 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41586
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
