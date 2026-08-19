# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 370
- HTTP: 244 alive / 91 gold
- HTTPS: 190 alive / 15 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 213 alive / 123 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18278
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
