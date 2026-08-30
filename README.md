# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 430
- HTTP: 136 alive / 85 gold
- HTTPS: 77 alive / 32 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44085
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
