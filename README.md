# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 399
- HTTP: 268 alive / 96 gold
- HTTPS: 193 alive / 31 gold
- SOCKS4: 202 alive / 146 gold
- SOCKS5: 238 alive / 126 gold

## Historical pool

- Discovered: 161007
- Ever alive: 31004
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
