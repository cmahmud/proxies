# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 424
- HTTP: 118 alive / 76 gold
- HTTPS: 147 alive / 21 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42362
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
