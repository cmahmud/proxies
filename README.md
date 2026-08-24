# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 437
- HTTP: 118 alive / 81 gold
- HTTPS: 67 alive / 25 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34157
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
