# SyndProxy private pool

## Current pool

- Alive now: 1133
- Gold now: 405
- HTTP: 376 alive / 78 gold
- HTTPS: 221 alive / 14 gold
- SOCKS4: 272 alive / 155 gold
- SOCKS5: 264 alive / 158 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20686
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
