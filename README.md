# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 476
- HTTP: 137 alive / 98 gold
- HTTPS: 131 alive / 41 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45095
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
