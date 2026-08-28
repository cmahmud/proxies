# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 427
- HTTP: 116 alive / 81 gold
- HTTPS: 147 alive / 20 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42256
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
