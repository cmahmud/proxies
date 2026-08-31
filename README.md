# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 446
- HTTP: 144 alive / 81 gold
- HTTPS: 102 alive / 32 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 223 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45446
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
