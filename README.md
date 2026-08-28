# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 425
- HTTP: 115 alive / 81 gold
- HTTPS: 158 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42299
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
