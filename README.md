# SyndProxy private pool

## Current pool

- Alive now: 1163
- Gold now: 443
- HTTP: 405 alive / 103 gold
- HTTPS: 231 alive / 28 gold
- SOCKS4: 258 alive / 153 gold
- SOCKS5: 269 alive / 159 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30439
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
