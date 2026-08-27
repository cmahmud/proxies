# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 425
- HTTP: 120 alive / 76 gold
- HTTPS: 168 alive / 24 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40495
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
