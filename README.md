# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 384
- HTTP: 287 alive / 88 gold
- HTTPS: 226 alive / 26 gold
- SOCKS4: 231 alive / 123 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 164181
- Ever alive: 32051
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
