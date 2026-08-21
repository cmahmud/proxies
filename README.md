# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 412
- HTTP: 311 alive / 107 gold
- HTTPS: 197 alive / 28 gold
- SOCKS4: 222 alive / 132 gold
- SOCKS5: 235 alive / 145 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30641
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
