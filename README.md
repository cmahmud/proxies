# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 435
- HTTP: 126 alive / 78 gold
- HTTPS: 80 alive / 25 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34147
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
