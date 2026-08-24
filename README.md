# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 428
- HTTP: 136 alive / 78 gold
- HTTPS: 63 alive / 22 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33940
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
