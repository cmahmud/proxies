# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 397
- HTTP: 386 alive / 103 gold
- HTTPS: 262 alive / 23 gold
- SOCKS4: 203 alive / 125 gold
- SOCKS5: 303 alive / 146 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22635
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
