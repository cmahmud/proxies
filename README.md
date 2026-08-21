# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 407
- HTTP: 240 alive / 90 gold
- HTTPS: 181 alive / 22 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 244 alive / 154 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27798
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
