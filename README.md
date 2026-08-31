# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 476
- HTTP: 161 alive / 100 gold
- HTTPS: 131 alive / 41 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45214
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
