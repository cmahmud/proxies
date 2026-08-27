# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 426
- HTTP: 116 alive / 79 gold
- HTTPS: 151 alive / 19 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42174
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
