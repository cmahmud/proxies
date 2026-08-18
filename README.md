# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 225
- HTTP: 225 alive / 32 gold
- HTTPS: 144 alive / 8 gold
- SOCKS4: 208 alive / 113 gold
- SOCKS5: 206 alive / 72 gold

## Historical pool

- Discovered: 93732
- Ever alive: 9327
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
