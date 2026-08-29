# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 382
- HTTP: 84 alive / 62 gold
- HTTPS: 90 alive / 14 gold
- SOCKS4: 163 alive / 152 gold
- SOCKS5: 173 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43318
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
