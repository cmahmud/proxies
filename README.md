# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 437
- HTTP: 114 alive / 75 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 205 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45556
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
