# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 407
- HTTP: 108 alive / 69 gold
- HTTPS: 160 alive / 15 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40956
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
