# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 479
- HTTP: 166 alive / 104 gold
- HTTPS: 121 alive / 39 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45207
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
