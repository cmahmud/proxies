# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 221
- HTTP: 226 alive / 32 gold
- HTTPS: 147 alive / 8 gold
- SOCKS4: 205 alive / 111 gold
- SOCKS5: 198 alive / 70 gold

## Historical pool

- Discovered: 93732
- Ever alive: 9327
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
