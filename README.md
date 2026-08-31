# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 447
- HTTP: 114 alive / 81 gold
- HTTPS: 112 alive / 32 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45631
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
