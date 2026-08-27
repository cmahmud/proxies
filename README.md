# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 425
- HTTP: 109 alive / 76 gold
- HTTPS: 182 alive / 22 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40548
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
