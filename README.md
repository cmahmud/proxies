# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 434
- HTTP: 411 alive / 102 gold
- HTTPS: 251 alive / 28 gold
- SOCKS4: 260 alive / 150 gold
- SOCKS5: 266 alive / 154 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30437
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
