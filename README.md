# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 445
- HTTP: 108 alive / 83 gold
- HTTPS: 74 alive / 32 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44600
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
