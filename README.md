# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 261
- HTTP: 354 alive / 36 gold
- HTTPS: 213 alive / 9 gold
- SOCKS4: 236 alive / 143 gold
- SOCKS5: 181 alive / 73 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13718
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
