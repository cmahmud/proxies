# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 425
- HTTP: 116 alive / 81 gold
- HTTPS: 176 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42306
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
