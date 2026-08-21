# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 412
- HTTP: 332 alive / 87 gold
- HTTPS: 239 alive / 25 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 265 alive / 155 gold

## Historical pool

- Discovered: 156427
- Ever alive: 29522
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
