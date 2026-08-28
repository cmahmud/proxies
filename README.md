# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 426
- HTTP: 116 alive / 82 gold
- HTTPS: 164 alive / 17 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42301
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
