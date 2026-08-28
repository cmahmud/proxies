# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 434
- HTTP: 120 alive / 86 gold
- HTTPS: 144 alive / 21 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42259
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
