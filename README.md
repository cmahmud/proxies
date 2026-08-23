# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 364
- HTTP: 79 alive / 44 gold
- HTTPS: 53 alive / 8 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 198 alive / 158 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
