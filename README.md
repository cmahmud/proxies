# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 392
- HTTP: 170 alive / 65 gold
- HTTPS: 54 alive / 15 gold
- SOCKS4: 182 alive / 154 gold
- SOCKS5: 202 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33136
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
