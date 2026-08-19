# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 416
- HTTP: 398 alive / 91 gold
- HTTPS: 285 alive / 22 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 280 alive / 161 gold

## Historical pool

- Discovered: 136185
- Ever alive: 22303
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
