# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 385
- HTTP: 414 alive / 94 gold
- HTTPS: 288 alive / 22 gold
- SOCKS4: 223 alive / 125 gold
- SOCKS5: 297 alive / 144 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22127
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
