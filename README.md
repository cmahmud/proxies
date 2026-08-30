# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 484
- HTTP: 146 alive / 101 gold
- HTTPS: 124 alive / 45 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44942
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
