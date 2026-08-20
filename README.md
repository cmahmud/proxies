# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 409
- HTTP: 226 alive / 79 gold
- HTTPS: 169 alive / 21 gold
- SOCKS4: 216 alive / 154 gold
- SOCKS5: 213 alive / 155 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27397
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
