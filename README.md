# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 464
- HTTP: 126 alive / 92 gold
- HTTPS: 123 alive / 31 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 215 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45975
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
