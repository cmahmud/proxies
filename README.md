# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 401
- HTTP: 87 alive / 58 gold
- HTTPS: 70 alive / 15 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41552
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
