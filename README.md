# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 420
- HTTP: 398 alive / 86 gold
- HTTPS: 270 alive / 14 gold
- SOCKS4: 255 alive / 156 gold
- SOCKS5: 274 alive / 164 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20723
- Ever gold: 874

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
