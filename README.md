# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 253
- HTTP: 197 alive / 30 gold
- HTTPS: 108 alive / 8 gold
- SOCKS4: 237 alive / 123 gold
- SOCKS5: 225 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9106
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
