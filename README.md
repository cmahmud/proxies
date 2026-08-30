# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 441
- HTTP: 113 alive / 86 gold
- HTTPS: 64 alive / 33 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44095
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
