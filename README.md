# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 476
- HTTP: 152 alive / 104 gold
- HTTPS: 134 alive / 36 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
