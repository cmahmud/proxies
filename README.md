# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 430
- HTTP: 115 alive / 81 gold
- HTTPS: 152 alive / 18 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42328
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
