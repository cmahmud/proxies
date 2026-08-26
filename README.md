# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 408
- HTTP: 135 alive / 72 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40370
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
