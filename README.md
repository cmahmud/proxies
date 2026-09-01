# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 459
- HTTP: 129 alive / 85 gold
- HTTPS: 126 alive / 35 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 185 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46706
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
