# SyndProxy private pool

## Current pool

- Alive now: 1700
- Gold now: 601
- HTTP: 730 alive / 216 gold
- HTTPS: 559 alive / 118 gold
- SOCKS4: 172 alive / 104 gold
- SOCKS5: 239 alive / 163 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24760
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
