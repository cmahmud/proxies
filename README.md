# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 398
- HTTP: 78 alive / 54 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41578
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
