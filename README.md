# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 424
- HTTP: 85 alive / 69 gold
- HTTPS: 85 alive / 26 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47136
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
