# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 396
- HTTP: 78 alive / 58 gold
- HTTPS: 33 alive / 15 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42854
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
