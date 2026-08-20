# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 361
- HTTP: 174 alive / 71 gold
- HTTPS: 109 alive / 20 gold
- SOCKS4: 176 alive / 126 gold
- SOCKS5: 193 alive / 144 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25601
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
