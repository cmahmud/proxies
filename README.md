# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 599
- HTTP: 423 alive / 183 gold
- HTTPS: 276 alive / 113 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 226 alive / 156 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19440
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
