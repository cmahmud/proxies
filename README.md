# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 387
- HTTP: 115 alive / 63 gold
- HTTPS: 40 alive / 12 gold
- SOCKS4: 186 alive / 154 gold
- SOCKS5: 207 alive / 158 gold

## Historical pool

- Discovered: 175423
- Ever alive: 33130
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
