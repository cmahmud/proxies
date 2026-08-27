# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 402
- HTTP: 90 alive / 59 gold
- HTTPS: 166 alive / 15 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41027
- Ever gold: 1316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
