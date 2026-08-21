# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 430
- HTTP: 342 alive / 109 gold
- HTTPS: 231 alive / 36 gold
- SOCKS4: 245 alive / 145 gold
- SOCKS5: 247 alive / 140 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30792
- Ever gold: 1148

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
