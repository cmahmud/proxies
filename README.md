# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 430
- HTTP: 119 alive / 85 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 198 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42267
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
