# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 359
- HTTP: 189 alive / 76 gold
- HTTPS: 134 alive / 23 gold
- SOCKS4: 217 alive / 143 gold
- SOCKS5: 178 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25348
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
