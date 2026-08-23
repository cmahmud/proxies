# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 387
- HTTP: 111 alive / 63 gold
- HTTPS: 91 alive / 13 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 188 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33138
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
