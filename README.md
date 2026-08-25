# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 427
- HTTP: 142 alive / 69 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 207 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36004
- Ever gold: 1263

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
