# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 417
- HTTP: 105 alive / 69 gold
- HTTPS: 187 alive / 22 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40626
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
