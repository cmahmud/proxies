# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 478
- HTTP: 167 alive / 104 gold
- HTTPS: 118 alive / 38 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45206
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
