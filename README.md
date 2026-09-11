# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 439
- HTTP: 107 alive / 79 gold
- HTTPS: 47 alive / 27 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49171
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
