# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 399
- HTTP: 76 alive / 58 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42825
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
