# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 417
- HTTP: 97 alive / 61 gold
- HTTPS: 65 alive / 25 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45488
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
