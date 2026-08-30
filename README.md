# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 445
- HTTP: 127 alive / 81 gold
- HTTPS: 152 alive / 33 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44708
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
