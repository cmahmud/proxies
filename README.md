# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 318
- HTTP: 291 alive / 48 gold
- HTTPS: 183 alive / 10 gold
- SOCKS4: 197 alive / 131 gold
- SOCKS5: 199 alive / 129 gold

## Historical pool

- Discovered: 128143
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
