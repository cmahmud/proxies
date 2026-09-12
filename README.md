# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 459
- HTTP: 124 alive / 94 gold
- HTTPS: 59 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49343
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
