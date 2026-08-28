# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 442
- HTTP: 121 alive / 86 gold
- HTTPS: 141 alive / 22 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42227
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
