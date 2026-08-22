# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 417
- HTTP: 280 alive / 85 gold
- HTTPS: 200 alive / 28 gold
- SOCKS4: 197 alive / 135 gold
- SOCKS5: 255 alive / 169 gold

## Historical pool

- Discovered: 161926
- Ever alive: 31193
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
