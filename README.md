# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 402
- HTTP: 80 alive / 58 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42851
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
