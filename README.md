# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 423
- HTTP: 121 alive / 75 gold
- HTTPS: 136 alive / 22 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 197 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42394
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
