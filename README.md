# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 450
- HTTP: 127 alive / 81 gold
- HTTPS: 86 alive / 34 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 203 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45593
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
