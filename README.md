# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 450
- HTTP: 148 alive / 92 gold
- HTTPS: 87 alive / 35 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 198 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44187
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
