# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 390
- HTTP: 94 alive / 58 gold
- HTTPS: 34 alive / 13 gold
- SOCKS4: 181 alive / 156 gold
- SOCKS5: 192 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33341
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
