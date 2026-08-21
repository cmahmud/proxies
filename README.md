# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 420
- HTTP: 231 alive / 94 gold
- HTTPS: 129 alive / 28 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 231 alive / 158 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29414
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
