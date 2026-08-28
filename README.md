# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 407
- HTTP: 89 alive / 64 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42703
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
