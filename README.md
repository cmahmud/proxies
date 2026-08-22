# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 428
- HTTP: 297 alive / 84 gold
- HTTPS: 189 alive / 25 gold
- SOCKS4: 226 alive / 154 gold
- SOCKS5: 264 alive / 165 gold

## Historical pool

- Discovered: 163866
- Ever alive: 31988
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
