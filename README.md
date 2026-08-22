# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 394
- HTTP: 278 alive / 92 gold
- HTTPS: 226 alive / 30 gold
- SOCKS4: 211 alive / 146 gold
- SOCKS5: 237 alive / 126 gold

## Historical pool

- Discovered: 161010
- Ever alive: 31009
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
