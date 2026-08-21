# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 433
- HTTP: 346 alive / 99 gold
- HTTPS: 231 alive / 27 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 261 alive / 163 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28754
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
