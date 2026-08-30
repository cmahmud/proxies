# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 437
- HTTP: 123 alive / 92 gold
- HTTPS: 68 alive / 35 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 174 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44092
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
