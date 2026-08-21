# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 367
- HTTP: 401 alive / 95 gold
- HTTPS: 254 alive / 22 gold
- SOCKS4: 191 alive / 116 gold
- SOCKS5: 228 alive / 134 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28816
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
