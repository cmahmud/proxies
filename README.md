# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 417
- HTTP: 289 alive / 84 gold
- HTTPS: 195 alive / 28 gold
- SOCKS4: 194 alive / 135 gold
- SOCKS5: 255 alive / 170 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31191
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
