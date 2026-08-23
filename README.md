# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 388
- HTTP: 118 alive / 64 gold
- HTTPS: 88 alive / 13 gold
- SOCKS4: 178 alive / 153 gold
- SOCKS5: 197 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33143
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
