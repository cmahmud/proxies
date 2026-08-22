# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 423
- HTTP: 261 alive / 92 gold
- HTTPS: 201 alive / 28 gold
- SOCKS4: 201 alive / 145 gold
- SOCKS5: 237 alive / 158 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31545
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
