# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 433
- HTTP: 121 alive / 85 gold
- HTTPS: 154 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 199 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42268
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
