# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 414
- HTTP: 104 alive / 72 gold
- HTTPS: 161 alive / 17 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40956
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
