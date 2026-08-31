# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 476
- HTTP: 163 alive / 102 gold
- HTTPS: 118 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45194
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
