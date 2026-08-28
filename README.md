# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 427
- HTTP: 121 alive / 79 gold
- HTTPS: 137 alive / 23 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42394
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
