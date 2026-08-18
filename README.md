# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 233
- HTTP: 333 alive / 30 gold
- HTTPS: 112 alive / 8 gold
- SOCKS4: 184 alive / 110 gold
- SOCKS5: 164 alive / 85 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6676
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
