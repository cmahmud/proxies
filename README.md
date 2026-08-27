# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 427
- HTTP: 114 alive / 79 gold
- HTTPS: 136 alive / 20 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42162
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
