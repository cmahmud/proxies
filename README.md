# SyndProxy private pool

## Current pool

- Alive now: 1234
- Gold now: 422
- HTTP: 470 alive / 96 gold
- HTTPS: 333 alive / 28 gold
- SOCKS4: 197 alive / 140 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 159271
- Ever alive: 30394
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
