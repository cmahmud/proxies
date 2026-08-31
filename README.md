# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 417
- HTTP: 115 alive / 64 gold
- HTTPS: 69 alive / 21 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45524
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
