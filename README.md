# SyndProxy private pool

## Current pool

- Alive now: 738
- Gold now: 409
- HTTP: 183 alive / 88 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 194 alive / 144 gold
- SOCKS5: 207 alive / 155 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27407
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
