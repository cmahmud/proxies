# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 411
- HTTP: 100 alive / 56 gold
- HTTPS: 66 alive / 27 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45509
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
