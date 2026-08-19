# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 437
- HTTP: 397 alive / 123 gold
- HTTPS: 254 alive / 42 gold
- SOCKS4: 211 alive / 128 gold
- SOCKS5: 252 alive / 144 gold

## Historical pool

- Discovered: 117103
- Ever alive: 17139
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
