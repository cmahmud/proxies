# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 447
- HTTP: 128 alive / 93 gold
- HTTPS: 66 alive / 33 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 203 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44252
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
