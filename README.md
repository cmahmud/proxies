# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 407
- HTTP: 104 alive / 54 gold
- HTTPS: 71 alive / 26 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45507
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
