# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 396
- HTTP: 79 alive / 56 gold
- HTTPS: 35 alive / 14 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42854
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
