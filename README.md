# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 392
- HTTP: 86 alive / 65 gold
- HTTPS: 78 alive / 15 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 166 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43359
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
