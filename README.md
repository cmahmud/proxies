# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 447
- HTTP: 120 alive / 82 gold
- HTTPS: 136 alive / 33 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44703
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
