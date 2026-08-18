# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 260
- HTTP: 251 alive / 28 gold
- HTTPS: 153 alive / 3 gold
- SOCKS4: 230 alive / 120 gold
- SOCKS5: 223 alive / 109 gold

## Historical pool

- Discovered: 99145
- Ever alive: 12068
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
